# Generated by Django 4.2.7 on 2023-12-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newarrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newimage', models.ImageField(upload_to='newimage')),
                ('description', models.TextField()),
                ('offer', models.CharField(max_length=100)),
            ],
        ),
    ]
