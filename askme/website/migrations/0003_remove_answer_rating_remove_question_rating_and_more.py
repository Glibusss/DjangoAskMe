# Generated by Django 4.2 on 2023-04-08 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_upvotequestion_upvoteanswer_downvotequestion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='question',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='relev',
        ),
    ]
