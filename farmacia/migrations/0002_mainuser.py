# Generated by Django 3.2.3 on 2021-09-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('usuario', models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario')),
                ('nombre', models.CharField(blank=True, max_length=256, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=256, null=True, verbose_name='Apellidos')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
