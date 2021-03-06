from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Horse, Jockey, Outcome, Profile, Experience
from .forms import OutcomeForm, ExperienceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

   
class HorseList(LoginRequiredMixin, ListView):
    model = Horse
    
    def get_queryset(self):
        return Horse.objects.filter(user=self.request.user)

@login_required
def horses_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    outcome_form = OutcomeForm()
    return render(request, 'horses/detail.html', {'horse' : horse, 'outcome_form': outcome_form})

@login_required
def add_horse_outcome(request, horse_id):
    form = OutcomeForm(request.POST)
    if form.is_valid():
        new_outcome = form.save(commit=False)
        new_outcome.horse_id = horse_id
        new_outcome.save()
    return redirect('detail', horse_id=horse_id)    

@login_required
def delete_horse_outcome(request, outcome_id):
    Outcome.objects.filter(id = outcome_id).delete()
    return redirect('/horses/')   

@login_required
def assoc_horse(request, jockey_id, horse_id):
    Jockey.objects.get(id=jockey_id).horses.add(horse_id)
    return redirect('jdetail', jockey_id=jockey_id)

@login_required
def unassoc_horse(request, jockey_id, horse_id):
    Jockey.objects.get(id=jockey_id).horses.remove(horse_id)
    return redirect('jdetail', jockey_id=jockey_id)    

class HorseCreate(LoginRequiredMixin, CreateView):
    model = Horse
    fields = ['name', 'age', 'description', 'starts', 'trainer', 'sire', 'dam']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class HorseUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = ['name', 'age', 'description', 'starts', 'trainer', 'sire', 'dam']

class HorseDelete(LoginRequiredMixin, DeleteView):
    model = Horse
    success_url = '/horses/'

class JockeyList(LoginRequiredMixin, ListView):
    model = Jockey
    
    def get_queryset(self):
        return Jockey.objects.filter(user=self.request.user)

@login_required
def jockeys_detail(request, jockey_id):
    jockey = Jockey.objects.get(id=jockey_id)
    not_ridden = Horse.objects.exclude(id__in = jockey.horses.all().values_list('id'))
    experience_form=ExperienceForm()
    return render(request, 'jockeys/jdetail.html', {'jockey' : jockey, 'experience_form': experience_form, 'horses' : not_ridden})

@login_required
def add_jockey_experience(request, jockey_id):
    form= ExperienceForm(request.POST)
    if form.is_valid():
        j_experience = form.save(commit=False)
        j_experience.jockey_id = jockey_id
        j_experience.save()
    return redirect('jdetail', jockey_id=jockey_id)     

@login_required
def delete_jockey_experience(request, experience_id):
    Experience.objects.filter(id = experience_id).delete()
    return redirect('/jockeys/')

class JockeyCreate(LoginRequiredMixin, CreateView):
    model = Jockey
    fields = ['age', 'name', 'bio', 'starts']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class JockeyUpdate(LoginRequiredMixin, UpdateView):
    model = Jockey
    fields = ['age', 'bio', 'starts']

class JockeyDelete(LoginRequiredMixin, DeleteView):
    model = Jockey
    success_url = '/jockeys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

