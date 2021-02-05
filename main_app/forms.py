from django.forms import ModelForm
from .models import Outcome, Experience
from django.contrib.auth.models import User
 

class OutcomeForm(ModelForm):
    class Meta:
        model = Outcome
        fields = ['name', 'date', 'outcome']


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['name', 'date', 'experience']        

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'password', 'firstname', 'lastname']        