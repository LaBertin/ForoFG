# Generated by Django 3.1.2 on 2020-11-05 19:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ForoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=600)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(null=True, upload_to='Noticia')),
            ],
        ),
    ]
