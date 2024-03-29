# Generated by Django 3.2 on 2021-05-02 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0002_auto_20210502_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Second_name', models.CharField(max_length=50)),
                ('cin', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=50, unique=True)),
                ('onset_state', models.TextField()),
                ('chronic', models.TextField()),
                ('vacc', models.BooleanField(default=False)),
                ('reinfect', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('hopital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.hospital')),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.medecin')),
            ],
        ),
    ]
