from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return HttpResponse(f"User {username} registered successfully!")
    return render(request, 'users/register.html')
