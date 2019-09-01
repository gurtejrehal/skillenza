from medical import views
from django.urls import path

app_name = 'medical'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-entry/', views.new_entry, name='new_entry'),
    path('search/', views.search, name='search'),
    path('get-result/', views.get_result, name='get_result'),
    path('edit/<int:acc_id>/', views.edit, name='edit_form'),
    path('dashboard/<int:acc_id>/', views.dashboard, name='dashboard'),
]
