# Generated by Django 4.0 on 2021-12-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_cotizaciones_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizaciones',
            name='status',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]
