from django.shortcuts import render

# Create your views here.

def dog_post_page(requests):
    return render(requests, 'dog_post/dog_post_form.html')

def dog_post_detail(requests):
    return render(requests, 'dog_post/dog_post_detail.html')

def dog_post_edit_page(requests):
    return render(requests, 'dog_post/dog_post_form_edit.html')

def deleate_dog_post(requests):
    return render(requests, 'dog_post/dog_post_confirm_delete.html')