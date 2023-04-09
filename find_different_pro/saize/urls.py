from django.urls import path ,include
from .views import model_form_upload
urlpatterns = [
    path('upload', model_form_upload,name='upload')
]
