from django import forms
from .models import Page


class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = [

			'title',
			'content',
			'image',

		]

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}