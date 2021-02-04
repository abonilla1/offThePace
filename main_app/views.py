from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Horse, Jockey, Outcome
from .forms import OutcomeForm

# Create your views here.

def home(request):
    return render(request, 'home.html')
   

class HorseList(ListView):
    model = Horse

class HorseDetail(DetailView):
    model = Horse

def add_outcome(request, horse_id):
    form = OutcomeForm(request.POST)
    if form.is_valid():
        new_outcome = form.save(commit=False)
        new_outcome.horse_id = horse_id
        new_outcome.save()
    return redirect('detail', horse_id=horse_id)    

def assoc_jockey(request, horse_id, jockey_id):
    Horse.objects.get(id=horse_id).jockeys.add(jockey_id)
    return redirect('detail', horse_id= horse_id)

class HorseCreate(CreateView):
    model = Horse
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class HorseUpdate(UpdateView):
    model = Horse
    fields = ['age', 'description', 'starts', 'trainer', 'sire', 'dam']


class JockeyList(ListView):
    model = Jockey

class JockeyDetail(DetailView):
    model = Jockey


def add_outcome(request, jockey_id):
    form = OutcomeForm(request.POST)
    if form.is_valid():
        new_outcome = form.save(commit=False)
        new_outcome.jockey_id = jockey_id
        new_outcome.save()
    return redirect('detail', jockey_id=jockey_id)     


class JockeyCreate(CreateView):
    model = Jockey
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class JockeyUpdate(UpdateView):
    model = Jockey
    fields = ['age', 'bio', 'starts']


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
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

