# Generated by Django 5.0.6 on 2024-06-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentData', '0002_alter_studentregistrationmodel_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.TextField(null=True)),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
