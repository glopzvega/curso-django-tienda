# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

# from django.contrib.auth.forms import UserCreationForm
from .forms import AccountModelForm

def registro(request):

	if request.method == "POST":

		form = AccountModelForm(request.POST)

		if form.is_valid():
			form.save()
			# username = form.cleaned_data["username"]
			# password = form.cleaned_data["password"]
			# email = form.cleaned_data["email"]			
			# user = User.objects.create_user(username, email, password)

		return redirect("/productos/")

	else:

		form = AccountModelForm()

	return render(request, "clientes/registro.html", {"form" : form })

