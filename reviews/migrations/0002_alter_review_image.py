# Generated by Django 3.2.4 on 2024-05-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(default='../default_post_fe0uhn', upload_to='images/'),
        ),
    ]
