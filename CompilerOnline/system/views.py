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
from .forms import StudentForm, ContainerForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError
from django.db.models import Q
import json

# Create your views here.
def users_form(request):
    return render(request,'system/users_form.html')

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect

def users_form(request):
    if request.method == 'POST':
        name_u = request.POST['name_u']
        email = request.POST['email']
        password = request.POST['password']
        role_id = request.POST.get('roles_id')
        hashed_password = make_password(password)
        
        if name_u and email and password:
            try:
                '''
                if Users.objects.filter(Q(name_u=name_u) | Q(email=email)).exists():
                    raise ValidationError('Ya existe un usuario con este nombre de usuario o correo electrónico')
                '''
                
                user = Users(name_u=name_u, email=email,password=hashed_password,roles_id_id=role_id)
                user.save()
                messages.success(request,f'Usuario {name_u} creado')
                return render(request, 'system/login/login.html')
            except IntegrityError:
                messages.error(request, 'Este email ya está registrado')
        else:
            messages.error(request, 'Por favor ingresar todos los campos')
    
    return render(request, 'system/users_form.html')

def students_form(request,id):
    return render(request,'system/students_form.html')

def students_form(request,id):
    user  = Users.objects.get(id=id)
    context = {
        'user_id':id
    }
    
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        pregunta = request.POST['pregunta']
        response_u = request.POST['response_u']
        
        if name and last_name and pregunta and response_u:
            
            student = Students.objects.filter(users_id_id=id)
            
            if student:
                    
                student.name = name
                student.last_name = last_name
                student.question_u =  pregunta
                student.response_u = response_u
                student.save()
                messages.success(request,f'Datos de {name} actualizados')
                context = {
                    'user_id':id
                }
                url = settings.BASE_URL + reverse('gestion_archivos',kwargs={'id':id})
                return redirect(url)
                
                
            else:
                
                student = Students(name=name,last_name=last_name,question_u=pregunta,response_u=response_u,users_id_id=id)
                student.save()
                messages.success(request,f'Datos de {name} actualizado')
                context = {
                    'user_id':id
                }
                url = settings.BASE_URL + reverse('gestion_archivos',kwargs={'id':id})
                return redirect(url)
            
        else:
            
            messages.error()
            
    else: 
        
        return render(request,'system/students_form.html',context)

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
            # bueno
                messages.error(request, 'No se encontró una cuenta asociada con este correo electrónico.')
                return render(request, 'system/login/login.html')
            
            if not check_password(password, user.password):
                messages.error(request, 'La contraseña es incorrecta.')
                return render(request, 'system/login/login.html')
            
            request.session['user_id'] = user.id
            request.session['email'] = email
            request.session['name_u'] = user.name_u
            context={
                'nombre_u':request.session['name_u'],
                'id':request.session['user_id']
            }
            url = settings.BASE_URL + reverse('gestion_archivos',kwargs={'id':user.id})
            return redirect(url)
            
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
    question = Students.objects.get(users_id_id=id)
    context = {
        'user_id':id,
        'question_user':question.question_u
    }
    return render(request, 'system/login/verificar_pp.html',context)

def verificar_pp(request,id):
    user_email  = Users.objects.get(id=id)
    user_editable = Students.objects.get(users_id=user_email)
    context = {
        'user_id':id,
        'question_user':user_editable.question_u
    }
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
    return render(request,'system/login/verificar_pp.html',context)

def cambiar_pass(request,id):
    return render(request, 'system/login/cambiar_pass.html')

def cambiar_pass(request,id):
    context = {
        'user_id':id
    }
    user = Users.objects.get(id = id)
    if request.method == 'POST':
        password = request.POST['password']
        new_password = request.POST['new-password']
        
        if password == new_password:
            hashed_password = make_password(password)
            user = Users(password=hashed_password)
            user.save()
            messages.success(request,f'Contraseña de {user.name_u} cambiada')
            
            return render(request, 'system/login/login.html')
        else:
            messages.error()
    else:
        return render(request, 'system/login/cambiar_pass.html',context)

def compilador(request,id,idProyect):
    return render(request, 'system/compilador/compilador.html')

def compilador(request,id,idProyect):
    user = Users.objects.get(id=id)
    
    try: 
        user_student = Students.objects.get(users_id_id=id)
        try:
            name = user_student.name
        except AttributeError:
            name=None
    except Students.DoesNotExist:
        name = None
        
    try:
        containers = Container.objects.filter(students_id_id = id)
    except Container.DoesNotExist:
        containers = None
    
    if name != None:   
        if containers != None:
            try:
                projects = Projects.objects.all()
            except Projects.DoesNotExist:
                projects = None             
    else:
        projects = None    
    
    projectId = None
    
    if request.method == 'POST':
        projectId  = request.POST.get('projectId','')
        print(projectId)
    
    try:
        projectCompiler = Projects.objects.get(id=idProyect)
    except Projects.DoesNotExist:
        projectCompiler = None

    context = {
        'user_id':id,
        'user':user,
        'name':name,
        'containers':containers,
        'projects':projects,
        'projectId':projectId,
        'idProyect':idProyect,
        'projectCompiler':projectCompiler
    }
    
    if request.method == 'POST':
        #description = request.POST['description']
        description = request.POST.get('description', '')
        #carpet = request.POST['id_carpeta']
        carpet = request.POST.get('id_carpeta','')
        #code = request.POST['code']
        code = request.POST.get('code','')
        
        if description and carpet and code:
            try:
                project = Projects(descripcion=description,data_ref=code,container_id_id=carpet,check_complete=1)
                project.save()
                return render(request, 'system/perfil/gestion_archivos.html',context)
            except IntegrityError:
                messages.error('')
    
    return render(request, 'system/compilador/compilador.html',context)

def compilador_no_user(request):
    return render(request, 'system/compilador_no_user/compilador_no_user.html')

def gestion_archivos(request,id):
    return render(request, 'system/perfil/gestion_archivos.html')

def gestion_archivos(request,id):
    user_email  = Users.objects.get(id=id)    
    
    try: 
        user_student = Students.objects.get(users_id_id=id)
        try:
            name = user_student.name
        except AttributeError:
            name=None
    except Students.DoesNotExist:
        name = None
    
    try:
        containers = Container.objects.filter(students_id_id = id)
    except Container.DoesNotExist:
        containers = None
            
    if name != None:   
        if containers != None:
            containers_id = []
            for container in containers:
                containers_id.append(container.id)
            
            try:
                projects = Projects.objects.all()
            except Projects.DoesNotExist:
                projects = None
            '''
            if projects != None:
                contador = containers.count()
                
                for i in range(contador):
                    aux_array = []
                    for project in projects:
                        if project.container_id_id == i:
                            aux_array.append(project)
                    diccionario = {}
                    diccionario[i]=aux_array'''
                         
    else:
        projects = None
    
    context = {
        'user_id':id,
        'name_u':user_email.name_u,
        'name':name,
        'form': ContainerForm(),
        'containers':containers,
        'projects':projects,
    }
    
    return render(request, 'system/perfil/gestion_archivos.html',context)

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
    form_class = ContainerForm
    template_name = 'system/container_form.html'
    success_url = reverse_lazy('container_list')
    success_message = "El contenedor se ha creado con éxito."

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            container_list = Container.objects.all()
            container_list_html = render_to_string('system/container_list.html', {'container_list': container_list})
            return JsonResponse({'container_list_html': container_list_html})
        else:
            messages.success(self.request, self.success_message)
            return response

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', self.success_url)


class ContainerUpdateView(UpdateView):
    model = Container
    fields = ['title']

'''
class ContainerDeleteView(DeleteView):
    model = Container
    success_url = reverse_lazy('container_list') 
    template_name = 'container_confirm_delete.html' '''

def container_delete(request, container_id):
    container = Container.objects.get(id=container_id)
    container.delete()
    return redirect(request.META['HTTP_REFERER'])

def projects_delete(request, project_id):
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect(request.META['HTTP_REFERER'])

def container_create_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        student_id = request.POST['students_id']
        student = Students.objects.get(id=student_id)
        container = Container(title=title, students=student)
        container.save()
        messages.success(request, 'El contenedor se ha creado con éxito.')
        return redirect('container_list')
    else:
        messages.error(request, 'Ha ocurrido un error al crear el contenedor.')
        return render(request, 'system/container_form.html')
 
def container_create_modal_view(request):
    form = ContainerForm()
    return render(request, 'system/container_form_modal.html', {'form': form})

def projects_view(request):
    containerId = request.GET.get('container_id')
    projects = Projects.objects.filter(container_id_id=containerId).values('id','descripcion','created')
    return JsonResponse(list(projects), safe=False)
