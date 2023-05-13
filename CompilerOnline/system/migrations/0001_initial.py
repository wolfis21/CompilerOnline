# Generated by Django 4.2 on 2023-05-12 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Carpeta',
                'verbose_name_plural': 'Carpetas',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rol', models.CharField(max_length=200, verbose_name='nombre del Rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_u', models.CharField(max_length=200, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico')),
                ('password', models.CharField(max_length=200, verbose_name='Contraseña')),
                ('roles_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.roles')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'system_users',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre de Estudiante')),
                ('last_name', models.CharField(max_length=200, verbose_name='apellido de Estudiante')),
                ('question_u', models.CharField(max_length=200, verbose_name='Pregunta de seguridad')),
                ('response_u', models.CharField(max_length=200, verbose_name='Respuesta correcta')),
                ('users_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='system.users')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('data_ref', models.CharField(max_length=200, verbose_name='ruta de archivo')),
                ('check_complete', models.BooleanField(default=False, verbose_name='Completado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('container_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.container')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.AddField(
            model_name='container',
            name='students_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='containers', to='system.students'),
        ),
    ]
