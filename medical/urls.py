from medical import views
from django.urls import path

app_name = 'medical'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-result/', views.get_result, name='get_result')
]
