from django.urls import path
from . import views
from .views import *
from .views import login_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
        #manejo de login
    path('login/', LoginView.as_view(template_name='system/login/login.html'), name='login_view'),
    path('login_view', views.login_view ,name='login_view'),
    path('recuperar_pass/', views.recuperar_pass, name='recuperar_pass'),
    path('verificar_pp/<str:id>', views.verificar_pp, name='verificar_pp'),
    path('cambiar_pass/<str:id>', views.cambiar_pass, name='cambiar_pass'),
        #fin login
        
    path('users_form/', views.users_form,name='users_form'),
    path('students_form/<str:id>', views.students_form,name='students_form'),
    
    #perfil
    path('gestion_archivos/<str:id>', views.gestion_archivos, name='gestion_archivos'),
    
   
    
    #compilador
    path('compilador/', views.compilador, name='compilador'),
    #compilador no login
    path('compilador_no_user/' , views.compilador_no_user, name='compilador_no_user'),
    
    #path('students/', StudentListView.as_view(), name='student_list'),
  #  path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    #path('students/create/', StudentCreateView.as_view(), name='student_create'),
    #path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    #path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('users/', UsersListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='user_detail'),
    path('users/create/', UsersCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UsersUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UsersDeleteView.as_view(), name='user_delete'),

    #Esto no se implementara
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('roles/create/', RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='role_update'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='role_delete'),

    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('containers/', ContainerListView.as_view(), name='container_list'),
    path('containers/<int:pk>/', ContainerDetailView.as_view(), name='container_detail'),
    path('containers/create/', ContainerCreateView.as_view(), name='container_create'),
    path('containers/create/modal/', container_create_modal_view, name='container_create_modal'),
    path('containers/<int:pk>/update/', ContainerUpdateView.as_view(), name='container_update'),
    path('containers/<int:pk>/delete/', ContainerDeleteView.as_view(), name='container_delete'),
]