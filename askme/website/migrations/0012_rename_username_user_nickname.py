# Generated by Django 4.2 on 2023-04-21 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='nickname',
        ),
    ]
