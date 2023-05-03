from django.shortcuts import render, redirect
from .models import Students, Users, Roles, Projects, Container, StudentsProjects
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Roles
from .forms import RoleForm, UsersForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'system/login.html')

class StudentListView(ListView):
    model = Students


class StudentDetailView(DetailView):
    model = Students


class StudentCreateView(CreateView):
    model = Students
    fields = ['name', 'last_name', 'question_u',
              'response_u','users_id']
    success_url = reverse_lazy('index')


class StudentUpdateView(UpdateView):
    model = Students
    fields = ['name', 'last_name', 'question_u',
              'response_u','users_id', 'students_projects']


class StudentDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('student_list')


class UsersListView(ListView):
    model = Users

class UsersDetailView(DetailView):
    model = Users

class UsersCreateView(CreateView):
    model = Users
    fields = ['name_u', 'email', 'password', 'roles_id']
    success_url = reverse_lazy('index')


class UsersUpdateView(UpdateView):
    model = Users
    fields = ['name_u', 'email', 'password', 'roles_id']
    success_url = reverse_lazy('index')

class UsersDeleteView(DeleteView):
    model = Users
    success_url = reverse_lazy('index')
class RoleListView(ListView):
    model = Roles


class RoleDetailView(DetailView):
    model = Roles


class RoleCreateView(CreateView):
    model = Roles
    form_class = RoleForm
    success_url = reverse_lazy('index')


class RoleUpdateView(UpdateView):
    model = Roles
    fields = ['name_rol']


class RoleDeleteView(DeleteView):
    model = Roles
    success_url = reverse_lazy('role_list')


class ProjectListView(ListView):
    model = Projects


class ProjectDetailView(DetailView):
    model = Projects


class ProjectCreateView(CreateView):
    model = Projects
    fields = ['descripcion', 'data_ref', 'check_complete', 'projects_students']


class ProjectUpdateView(UpdateView):
    model = Projects
    fields = ['descripcion', 'data_ref', 'check_complete', 'projects_students']


class ProjectDeleteView(DeleteView):
    model = Projects
    success_url = reverse_lazy('project_list')


class ContainerListView(ListView):
    model = Container


class ContainerDetailView(DetailView):
    model = Container


class ContainerCreateView(CreateView):
    model = Container
    fields = ['title']


class ContainerUpdateView(UpdateView):
    model = Container
    fields = ['title']


class ContainerDeleteView(DeleteView):
    model = Container
    success_url = reverse_lazy('container_list')
