from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('nombre', 'nombre')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "subtitulo","categoria", "autor", "texto")
        
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
        fields = ("titulo", "subtitulo", "categoria", "texto")
        
        widgets = {
            "titulo":forms.TextInput(attrs={'class':'form-control'}),
            "subtitulo":forms.TextInput(attrs={'class':'form-control'}),
            "categoria":forms.Select(choices=choices, attrs={'class':'form-control'}),
            "texto":forms.Textarea(attrs={'class':'form-control'}),
        }