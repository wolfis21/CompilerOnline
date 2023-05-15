from django.contrib import admin
from .models import Roles
from .models import Students
from .models import Users
from .models import Projects
from .models import Container

@admin.register(Roles)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('id','name_rol')


@admin.register(Students)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'last_name', 'question_u', 'response_u', 'users_id')
    search_fields = ('id','name', 'last_name')

@admin.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','name_u', 'email', 'password', 'roles_id')
    search_fields = ('name_u', 'email')

@admin.register(Projects)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion', 'data_ref', 'check_complete', 'created', 'updated', 'container_id')
    list_filter = ('descripcion','check_complete', 'created', 'updated')
    search_fields = ('descripcion','container_id')
    """ list_editable = ('title',)
 """
@admin.register(Container)

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'get_student_name')
    list_filter = ('title', 'created', 'updated', 'students_id')
    search_fields = ('title', 'created', 'updated', 'students_id__name', 'students_id__last_name')

    def get_student_name(self, obj):
        return f"{obj.students_id.name} {obj.students_id.last_name}" if obj.students_id else None
    get_student_name.short_description = "Estudiante"


