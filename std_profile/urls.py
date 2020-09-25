from . import views
from django.urls import path

app_name = 'std_profile'

urlpatterns = [


    path('', views.std_list),
    path('<int:pk>', views.std_detail, name='std_detail'),
    path('edit/<int:pk>/', views.edit, name = 'edit'),
    path('delet/<int:pk>/', views.std_delete, name = 'delet'),
]