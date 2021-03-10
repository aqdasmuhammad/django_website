from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("team", views.team, name='team'),
    path("contact", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("logout", views.logout, name='logout'),
    path("events", views.events, name='events'),
    path("complaint", views.complaint, name='complaint'),
    path("meeting", views.meeting, name='meeting'),
    path("report", views.report, name='report'),
]