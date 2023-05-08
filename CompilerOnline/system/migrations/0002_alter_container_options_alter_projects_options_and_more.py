# Generated by Django 4.2.1 on 2023-05-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='container',
            options={'verbose_name': 'Carpeta', 'verbose_name_plural': 'Carpetas'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterModelOptions(
            name='projectscontainer',
            options={'verbose_name': 'Projecto-Carpeta', 'verbose_name_plural': 'Proyectos-Carpetas'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Rol', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='studentsprojects',
            options={'verbose_name': 'Relacion Estudiante - Proyecto', 'verbose_name_plural': 'Relaciones'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electronico'),
        ),
        migrations.AlterModelTable(
            name='users',
            table='system_users',
        ),
    ]