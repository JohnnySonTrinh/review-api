# Generated by Django 3.2.4 on 2024-07-08 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='user',
            new_name='owner',
        ),
    ]