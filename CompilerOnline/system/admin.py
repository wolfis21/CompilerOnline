from django.contrib import admin

# Register your models here.
from .models import Roles
from .models import Students, StudentsProjects
from .models import Users
from .models import Projects, ProjectsContainer
from .models import Container

@admin.register(Roles)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('id','name_rol')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """

@admin.register(Students)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'last_name', 'question_u', 'response_u', 'users_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','name_u', 'email', 'password', 'roles_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(Projects)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion', 'data_ref', 'check_complete', 'created', 'updated')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(Container)

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created', 'updated')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(StudentsProjects)

class StudentsProjectsAdmin(admin.ModelAdmin):
    list_display = ('student_id','project_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """
@admin.register(ProjectsContainer)

class ProjectsContainerAdmin(admin.ModelAdmin):
    list_display = ('projects_id','container_id')
    """ list_editable = ('title',)
    list_filter = ('title', 'desc')
    search_fields = ('title', 'desc')
 """

