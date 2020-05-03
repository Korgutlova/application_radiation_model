from django.urls import path

from app.views import main

app_name = "app"

urlpatterns = [
    path(r'', main, name="main")
]
