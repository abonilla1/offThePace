from django.forms import ModelForm
from .models import Outcome
from django.contrib.auth.models import User
 

class OutcomeForm(ModelForm):
    class Meta:
        model = Outcome
        fields = ['date', 'outcome']

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'password', 'firstname', 'lastname']        