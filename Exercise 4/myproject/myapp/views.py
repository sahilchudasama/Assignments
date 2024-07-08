from django.shortcuts import render

def user_form(request):
    return render(request, 'user_form.html')
