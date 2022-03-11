from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, 
    PasswordResetCompleteView, LoginView, LogoutView
    )
from .views import *
from .forms import EmailValidationOnForgotPassword


urlpatterns = [
    # Profile urls
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit/$', profile_update, name='edit_profile'),
    url(r'^profile/change-password/$', change_password, name='change_password'),
    # End Profile urls

    # Registration url
    url(r'^registration/$', registration_page, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),

    url(r'^password-reset/$', PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPassword,
        template_name='accounts/password_reset.html'
    ),
         name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ),
         name='password_reset_done'),
    url(r'^password-reset-confirm/<uidb64>/<token>/$', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ),
         name='password_reset_confirm'),
    url(r'^password-reset-complete/$', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ),
         name='password_reset_complete')
    # End Registration url
]
