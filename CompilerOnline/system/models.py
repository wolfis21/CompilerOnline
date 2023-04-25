from django.db import models

# Create your models here.
#prototype 1
class Roles(models.Model):
    name_rol = models.CharField(max_length=200, verbose_name='nombre del Rol')

class Students(models.Model):
    name =models.CharField(max_length=200, verbose_name='nombre de Estudiante')
    last_name =models.CharField(max_length=200, verbose_name='apellido de Estudiante')
    question_u =models.CharField(max_length=200, verbose_name='Pregunta de seguridad')
    response_u =models.CharField(max_length=200, verbose_name='Respuesta correcta')
    students_projects = models.ManyToManyField('Projects')
    users_id=models.ForeignKey('Users', on_delete=models.CASCADE)


class Users(models.Model):
    name_u =models.CharField(max_length=200, verbose_name='nombre de usuario')
    email = models.EmailField()
    password =models.CharField(max_length=200, verbose_name='Contraseña')
    roles_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Projects(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    data_ref = models.CharField(max_length=200, verbose_name='ruta de archivo')
    check_complete=models.CharField(max_length=200, verbose_name='valor 1 o 0') #pensar en un valor booleano
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    projects_students =models.ManyToManyField(Students)

##Relacion m a n (pibote)

class StudentsProjects(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)


class Container(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')


##Relacion m a n (pibote)

class ProjectsContainer(models.Model):
    projects_id =models.ForeignKey(Projects, on_delete=models.CASCADE)
    container_id = models.ForeignKey(Container, on_delete=models.CASCADE)

