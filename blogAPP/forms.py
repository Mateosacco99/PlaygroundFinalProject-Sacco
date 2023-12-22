from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('nombre', 'nombre')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "subtitulo","categoria", "autor", "texto", "imagen")
        
        widgets = {
            "titulo":forms.TextInput(attrs={'class':'form-control'}),
            "subtitulo":forms.TextInput(attrs={'class':'form-control'}),
            "categoria":forms.Select(choices=choices, attrs={'class':'form-control'}),
            "autor":forms.TextInput(attrs={'class':'form-control', 'value':'' , 'id':'placeholder', 'type':'hidden'}),
            #"autor":forms.Select(attrs={'class':'form-control'}),
            "texto":forms.Textarea(attrs={'class':'form-control'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "subtitulo", "categoria", "texto", "imagen")
        
        widgets = {
            "titulo":forms.TextInput(attrs={'class':'form-control'}),
            "subtitulo":forms.TextInput(attrs={'class':'form-control'}),
            "categoria":forms.Select(choices=choices, attrs={'class':'form-control'}),
            "texto":forms.Textarea(attrs={'class':'form-control'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body","post")
        
        widgets = {
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "body":forms.Textarea(attrs={'class':'form-control'}),
        }