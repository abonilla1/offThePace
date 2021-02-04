from django.forms import ModelForm
from .models import Outcome


class OutcomeForm(ModelForm):
    class Meta:
        model = Outcome
        fields = ['date', 'outcome']

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'password', 'firstname', 'lastname']        