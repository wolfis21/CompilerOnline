from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
#prototype 1

class Roles(models.Model):
    name_rol = models.CharField(max_length=200, verbose_name='nombre del Rol')
    
    class Meta:
        verbose_name='Rol'
        verbose_name_plural='Roles'
        
    def __str__(self):
        return self.name_rol

class Students(models.Model):
    name =models.CharField(max_length=200, verbose_name='nombre de Estudiante')
    last_name =models.CharField(max_length=200, verbose_name='apellido de Estudiante')
    question_u =models.CharField(max_length=200, verbose_name='Pregunta de seguridad')
    response_u =models.CharField(max_length=200, verbose_name='Respuesta correcta')
    students_projects = models.ManyToManyField('Projects')
    users_id=models.ForeignKey('Users', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural='Estudiantes'

class Users(models.Model):
    name_u = models.CharField(max_length=200, verbose_name='Nombre de usuario')
    email = models.EmailField(verbose_name='Correo electronico')
    password =models.CharField(max_length=200, verbose_name='Contraseña')
    roles_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        db_table='system_users'
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        
    def __str__(self):
        return self.email
        
class Projects(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    data_ref = models.CharField(max_length=200, verbose_name='ruta de archivo')
    check_complete=models.CharField(max_length=200, verbose_name='valor 1 o 0') #pensar en un valor booleano
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    projects_students =models.ManyToManyField(Students)

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
##Relacion m a n (pibote)

class StudentsProjects(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Relacion Estudiante - Proyecto'
        verbose_name_plural='Relaciones'


class Container(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name='Carpeta'
        verbose_name_plural='Carpetas'

##Relacion m a n (pibote)

class ProjectsContainer(models.Model):
    projects_id =models.ForeignKey(Projects, on_delete=models.CASCADE)
    container_id = models.ForeignKey(Container, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Projecto-Carpeta'
        verbose_name_plural='Proyectos-Carpetas'

