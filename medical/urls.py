from medical import views
from django.urls import path

app_name = 'medical'

urlpatterns = [
    path('', views.index, name='index'),
]
