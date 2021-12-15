# Generated by Django 4.0 on 2021-12-14 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0003_alter_usuarios_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=75)),
                ('ubicacion', models.CharField(max_length=150)),
                ('mercado', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.RenameField(
            model_name='tareas',
            old_name='fecha_finalisacion',
            new_name='fecha_finalizacion',
        ),
        migrations.AlterField(
            model_name='cotisaciones',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='administrador_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador',
                                    to='auth.user'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='administrador_encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encargado',
                                    to='auth.user'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='administradores',
        ),
        migrations.DeleteModel(
            name='usuarios',
        ),
    ]
