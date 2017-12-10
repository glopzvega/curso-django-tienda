from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm, NumberInput, TextInput, Textarea, PasswordInput

class AccountModelForm(ModelForm):
	
	class Meta:
		model = User
		fields = ("username", "email", "password", "first_name", "last_name")
		labels = {
			'first_name' : 'Nombre',
			'last_name' : 'Apellido'
		}
		widgets = {
			'first_name' : forms.TextInput(attrs={'title' : 'Nombre'}),
            'password': forms.PasswordInput(),
        }
		# fields = "__all__" 		
