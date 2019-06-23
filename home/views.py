from django.shortcuts import render

# Create your views here.
def welcome_page(requests):
    return render(requests, 'home/welcome_page.html')