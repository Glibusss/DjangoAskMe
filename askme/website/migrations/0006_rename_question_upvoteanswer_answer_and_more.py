# Generated by Django 4.2 on 2023-04-09 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_question_authorid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upvoteanswer',
            old_name='question',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='upvotequestion',
            old_name='question',
            new_name='answer',
        ),
    ]
