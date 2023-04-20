from django.urls import path
from . import views
from .views import (
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView,
    RoleListView, RoleDetailView, RoleCreateView, RoleUpdateView, RoleDeleteView,
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
    ContainerListView, ContainerDetailView, ContainerCreateView, ContainerUpdateView, ContainerDeleteView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

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
    path('containers/<int:pk>/update/', ContainerUpdateView.as_view(), name='container_update'),
    path('containers/<int:pk>/delete/', ContainerDeleteView.as_view(), name='container_delete'),
]