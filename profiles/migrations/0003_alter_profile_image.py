# Generated by Django 3.2.4 on 2024-07-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20240427_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_xw5shd', upload_to='images/'),
        ),
    ]
