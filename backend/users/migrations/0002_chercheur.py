# Generated by Django 3.2 on 2021-05-02 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chercheur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firs_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('affiliation', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
