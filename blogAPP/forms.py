from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "subtitle", "author", "body")
        
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "subtitle":forms.TextInput(attrs={'class':'form-control'}),
            "author":forms.Select(attrs={'class':'form-control'}),
            "body":forms.Textarea(attrs={'class':'form-control'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "subtitle", "body")
        
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "subtitle":forms.TextInput(attrs={'class':'form-control'}),
            "body":forms.Textarea(attrs={'class':'form-control'}),
        }