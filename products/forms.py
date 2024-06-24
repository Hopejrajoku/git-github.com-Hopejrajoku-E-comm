from django import forms 

from .models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        labels = {'password2':'Confirm Password'}

        

"""
class FeedbackForm(forms.Form):
    name=forms.CharField(required=True, error_messages={"required":"You forgot to add your name!"},)
    rating=forms.IntegerField(min_value=1, max_value=5)
    text=forms.CharField(label="Your feedback:", widget=forms.Textarea, max_length=200)
    """

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','rating','text']
        labels = {'name':'Full name', 'text':'Your Feedback'}



