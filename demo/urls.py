from django.urls import path
from demo.views import (hello_reader)

urlpatterns = [
    path('home/', hello_reader, name="hello_reader")
]
