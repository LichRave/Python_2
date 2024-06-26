"""
URL configuration for countries project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import ListView
import django.contrib.auth.views as auth_views
from c_viewer.models import Country
from c_viewer.views import (
    CountriesCreateView,
    CountriesUpdateView,
    CountryDeleteView,
    CountriesList,
    SignUpView,
    UserClicksView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", CountriesList.as_view(), name="index"),
    path("form", CountriesCreateView.as_view(), name="form"),
    path("update_form/<pk>", CountriesUpdateView.as_view(), name="update_form"),
    path("delete/<pk>", CountryDeleteView.as_view(), name="delete"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("accounts/sign_up", SignUpView.as_view(), name="sign_up"),
    path("List_users_clicks", UserClicksView.as_view()),
]
