from django.urls import path
from . import views

urlpatterns = [
    path('persons_list/', views.person_list, name = 'person_list_page'),
		path('create_person/', views.person_create, name = 'person_create_page'),
		path('edit_person/<int:id>/', views.person_edit, name = 'person_edit_page'),
		path('delete_person/<int:id>/', views.person_delete, name = 'person_delete_option'),
		path('', views.person_list),
]

