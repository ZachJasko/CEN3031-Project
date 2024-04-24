from django import forms
from .models import *  

# UserPostForm for creating and editing UserPost objects
class UserPostForm(forms.ModelForm):
    title = forms.CharField( 
        label="",
        widget=forms.TextInput(attrs={ 
            'class': 'form-control form-control-style-3', 
            'placeholder': 'Title',
        })
    )

    description = forms.CharField(
        label="", 
        widget=forms.Textarea(attrs={ 
            'class': 'form-control form-control-style-3', 
            'placeholder': 'Description in detail...', 
            'rows': '8',  
            'cols': '80',  
        })
    )

    class Meta:
        model = UserPost  
        fields = ['title', 'description']  
        
# AnswerForm for creating and editing Answer objects  
class AnswerForm(forms.ModelForm):
    content = forms.CharField(  
        label="",  
        widget=forms.Textarea(attrs={  
            'class': 'form-control form-control-style-3',  # CSS classes
            'placeholder': 'Write your answer...',  
            'rows': '8',  
            'cols': '50',  
        })
    )

    class Meta:
        model = Answer  
        fields = ['content',] 
