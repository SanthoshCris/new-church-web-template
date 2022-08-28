from django.contrib import admin
from django.urls import path
from luzChurchAdmin.views import admin_instructions,homepage_section1, add_church_moto, add_history_office

urlpatterns = [
    # PAGE RENDER URLs
    path('instructions/', admin_instructions),
    path('homepage-section1/', homepage_section1),

    # API
    path('church-moto/',add_church_moto),
    path('church-office-history/',add_history_office)
]
