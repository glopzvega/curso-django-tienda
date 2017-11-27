# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .forms import AccountModelForm

def registro(request):

	if request.method == "POST":

		form = AccountModelForm(request.POST)

		if form.is_valid():

			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			email = form.cleaned_data["email"]
			
			user = User.objects.create_user(username, password, email)

			return redirect("/productos/")

	else:

		form = AccountModelForm()

	return render(request, "clientes/registro.html", {"form" : form })

