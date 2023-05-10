from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import RoleForm, UsersForm
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserCreationForm
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from .forms import StudentForm

# Create your views here.
def users_form(request):
    return render(request,'system/users_form.html')

def users_form(request):
    if request.method == 'POST':
        name_u = request.POST['name_u']
        email = request.POST['email']
        password = request.POST['password']
        role_id = request.POST.get('roles_id')
        hashed_password = make_password(password)
        
        if name_u and email and password:
            
            user = Users(name_u=name_u, email=email,password=hashed_password,roles_id_id=role_id)
            user.save()
            messages.success(request,f'Usuario {name_u} creado')
            
            #return redirect(reverse('system/login/login.html'))
            return render(request, 'system/login/login.html')
        else:
            messages.error()
    else: 
        return render(request, 'system/users_form.html')

def students_form(request):
    return render(request,'system/students_form.html')



def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'system/login/login.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        if email and password:
            '''
            user = authenticate(email=email,password=password)
            print(user)'''
            
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
            # Si el usuario no existe, mostrar un mensaje de error
                messages.error(request, 'No se encontró una cuenta asociada con este correo electrónico.')
                return render(request, 'system/login/login.html')
            
            if not check_password(password, user.password):
                return render(request, 'system/login/login.html', {'error_message': 'El correo o la contraseña son incorrectos'})
            
            request.session['user_id'] = user.id
            request.session['email'] = email
            request.session['name_u'] = user.name_u
            context={
                'nombre_u':request.session['name_u'],
                'id':request.session['user_id']
            }
            url = settings.BASE_URL + reverse('gestion_archivos',kwargs={'id':user.id})
            return redirect(url)
            '''return render(request,'system/perfil/gestion_archivos.html',context)'''
        else:
            messages.info(request, 'Missing email or password')
            return render('system/login/login.html')

    return render(request,'system/login/login.html')

def recuperar_pass(request):
    return render(request, 'system/login/recuperar_pass.html')

def recuperar_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            messages.error(request, 'No se encontró una cuenta asociada con este correo electrónico.')
            return redirect('recuperar_pass')
        else:
            subject = 'Recuperación de contraseña'
            link = settings.BASE_URL + reverse('verificar_pp',kwargs={'id':user.id})
            message = f'Hola {link}'
            from_email = 'zorrillaja30@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, 'Se ha enviado un correo electrónico con instrucciones para restablecer su contraseña.')
            
            return redirect('recuperar_pass')
    return render(request, 'system/login/recuperar_pass.html')

def verificar_pp(request,id):
    return render(request, 'system/login/verificar_pp.html')

def verificar_pp(request,id):
    user_email  = Users.objects.get(id=id)
    user_editable = Students.objects.get(users_id=user_email)
    
    if request.method == "POST":
        
        question_u = request.POST['question_u']
        response_u = request.POST['response_u']
        
        user_edit = Students.objects.get(question_u=question_u)
        response_edit = Students.objects.get(response_u=response_u)
        if response_u:
            if user_editable.response_u == response_u:
                url = settings.BASE_URL + reverse('cambiar_pass',kwargs={'id':id})
                return redirect(url)
            else:
                print('no')
    return render(request,'system/login/verificar_pp.html')

def cambiar_pass(request,id):
    user_email  = Users.objects.get(id=id)
    return render(request, 'system/login/cambiar_pass.html')

def cambiar_pass(request,id):
    return render(request, 'system/login/cambiar_pass.html')

def compilador(request):
    return render(request, 'system/compilador/compilador.html')

def compilador_no_user(request):
    return render(request, 'system/compilador_no_user/compilador_no_user.html')

def gestion_archivos(request,id):
    return render(request, 'system/perfil/gestion_archivos.html')

def gestion_archivos(request,id):
    user_email  = Users.objects.get(id=id)
    return render(request, 'system/perfil/gestion_archivos.html')

class StudentListView(ListView):
    model = Students


class StudentDetailView(DetailView):
    model = Students


class StudentCreateView(CreateView):
    model = Students
    form_class = StudentForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        # Validar los datos del formulario
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos
            return super().form_valid(form)
        else:
            return self.form_invalid(form)    


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
