# Generated by Django 5.1.2 on 2024-10-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questn', models.CharField(max_length=122)),
                ('questnId', models.CharField(max_length=122)),
                ('qname', models.CharField(max_length=122)),
                ('extra2', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Templeate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=122)),
                ('branch', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('extra3', models.CharField(max_length=122)),
            ],
        ),
    ]