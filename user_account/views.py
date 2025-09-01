from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def user_list(request):
    users = User.objects.all()
    return render(request, "users.html", {'users': users})