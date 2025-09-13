from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm


@login_required
def profile_view(request):
    """
    Displays the user's profile
    with options to update details or change password.
    """
    return render(request, "user_account/profile.html")


@login_required
def profile_update(request):
    """
    Allows users to update there profile information on a form.
    """
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'user_account/profile_update.html', {'form': form})


@login_required
def change_password(request):
    """
    Allows users to change their password using Django's built-in form.
    Keeps the user logged in after password change.
    """
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully!")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "user_account/change_password.html", {"form": form})
