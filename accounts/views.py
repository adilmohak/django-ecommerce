from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# from django.db.models import Sum, Avg, Max, Min, Count
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView, ListView
from django.core.paginator import Paginator
from .decorators import superuser_required, customer_required
from django.conf import settings
# from django.conf.urls.static import static
from django.utils.decorators import method_decorator
from .forms import *
from .models import *


# ########################################################
# Profile views
# ########################################################
@login_required
def profile(request):
    """ Show profile of any user that fire out the request """
    if request.user.is_customer:
        # level = Customer.objects.get(user__pk=request.user.id)
        # courses = TakenCourse.objects.filter(customer__user__id=request.user.id, course__level=level.level)
        context = {
            'title': request.user.get_full_name,
            # 'courses': courses,
            # 'level': level,
        }
        return render(request, 'accounts/profile.html', context)
    else:
        staff = User.objects.filter(is_superuser=True)
        return render(request, 'accounts/profile.html', {
            'title': request.user.get_full_name,
            "staff": staff,
        })


# ########################################################
# Setting views
# ########################################################
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile_setting.html', {
        'title': 'Setting | DjangoSMS',
        'form': form,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error(s) below. ')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form,
    })
# ########################################################


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account for " + first_name + ' ' + last_name + " has been created. You are now able to login."
                )
            return redirect("login")
    else:
        form = RegistrationForm()

    context = {
        'title': 'Lecturer Add | DjangoSMS',
        'form': form,
    }

    return render(request, 'accounts/register.html', context)