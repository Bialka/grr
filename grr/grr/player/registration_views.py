#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import render_to
from django import forms
from django.contrib.auth import (authenticate, forms as auth_forms, 
    login as auth_login)
from django.shortcuts import redirect


@render_to('registration/home.html')
def home(request):
    # get url to redirect to
    redirect_to = '/admin'  # TODO
    
    # redirect logged users
    if request.user.is_authenticated():
        return redirect(redirect_to)

    if request.method == "POST":
        if 'password2' in request.POST:
            registration_form = auth_forms.UserCreationForm(request.POST or None)
            if registration_form.is_valid():
                # create user
                user = registration_form.save()
                # log him in
                user = authenticate(username=user.username, 
                    password=request.POST['password1'])
                auth_login(request, user)
                # redirect
                return redirect(redirect_to)
                
            form = auth_forms.AuthenticationForm(request)
        else:
            # this is basically a copy from auth.login view
            form = auth_forms.AuthenticationForm(request, data=request.POST or None)
            if form.is_valid():
                auth_login(request, form.get_user())
                # redirect
                return redirect(redirect_to)
            registration_form = auth_forms.UserCreationForm()
    else:
        registration_form = auth_forms.UserCreationForm()
        form = auth_forms.AuthenticationForm(request)

    return {
        'form': form,
        'registration_form': registration_form,
    }
