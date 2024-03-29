# Generated by Django 3.2 on 2021-05-02 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medecin',
            name='id_prof',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medecin',
            name='phone',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
