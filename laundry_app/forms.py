from django import forms
from django.contrib.auth.models import User
from laundry_app.models import *



# learn section
class formExample(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget= forms.Textarea)

class personForm(forms.ModelForm):
    class Meta:
        model = person
        fields = "__all__"


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class userProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')