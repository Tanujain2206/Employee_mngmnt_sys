from django.urls import path,include
from  . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('view_emp/',views.view_emp ,name='view_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('remove/',views.remove,name='remove'),
    path('remove/<int:emp_id>',views.remove,name='remove'),
    path('filter/',views.filter,name='filter')
    
]