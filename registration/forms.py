from django.forms import ModelForm
# importing default user registration form
from django.contrib.auth.forms import UserCreationForm
# importing built-in user model
from django.contrib.auth.forms import User
from django import forms
from forum.models import Author

# Creating custom User registration form utilizing the default one
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith("@ufl.edu"):
            raise forms.ValidationError("Please use a valid @ufl.edu email address.")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
    class Meta:
        model = Author
        fields = ['is_moderator']
        

"""Utilizing both forms to let user's update their account's information"""
# Updating the User registration form
class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']
        exclude = ['user']

# Updating the profile form
class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['profile_pic', 'bio']