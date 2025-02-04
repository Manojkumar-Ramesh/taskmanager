# Generated by Django 5.0.1 on 2024-03-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
