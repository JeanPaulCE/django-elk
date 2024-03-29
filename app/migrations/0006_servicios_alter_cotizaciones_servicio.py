# Generated by Django 4.0 on 2021-12-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cotizaciones_delete_cotisaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='cotizaciones',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicios'),
        ),
    ]
