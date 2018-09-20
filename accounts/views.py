from django.shortcuts import render
from django.contrib import messages


def login(request):
    messages.info(request, 'Your login and password did not match. Please, try again.')
    return render(request, template_name)
