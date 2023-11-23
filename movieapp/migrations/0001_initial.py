# Generated by Django 4.2.6 on 2023-11-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('des', models.TextField(max_length=250)),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
