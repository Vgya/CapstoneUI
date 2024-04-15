#from django.urls import path
#from . import views

#urlpatterns =[
#    path("",views.home, name="home")
#]

# myapp/urls.py
from django.urls import path
from .views import file_upload_view

urlpatterns = [
    path('', file_upload_view, name='file_upload'),
]
