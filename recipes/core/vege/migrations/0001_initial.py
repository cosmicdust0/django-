# Generated by Django 5.0.4 on 2024-04-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_des', models.TextField()),
                ('recepies_image', models.ImageField(upload_to='')),
            ],
        ),
    ]