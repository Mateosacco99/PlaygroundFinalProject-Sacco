from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blogAPP.models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args: Any, **kwargs: Any):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("user", "bio", "profile_pic", "instagram_url")
        widgets = {
            
                "user":forms.TextInput(attrs={'class':'form-control', 'value':'' , 'id':'placeholder', 'type':'hidden'}),
                "bio":forms.Textarea(attrs={'class':'form-control'}),
                #"profile_pic":forms.TextInput(attrs={'class':'form-control'}),
                "instagram_url":forms.TextInput(attrs={'class':'form-control'}),
        }