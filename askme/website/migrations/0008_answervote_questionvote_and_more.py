# Generated by Django 4.2 on 2023-04-10 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_question_downvoteanswer_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='answerVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'like'), (-1, 'dislike')], default=1)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user')),
            ],
        ),
        migrations.CreateModel(
            name='questionVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 'like'), (-1, 'dislike')], default=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='downvotequestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='downvotequestion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='upvoteanswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='upvoteanswer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='upvotequestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='upvotequestion',
            name='user',
        ),
        migrations.DeleteModel(
            name='downvoteAnswer',
        ),
        migrations.DeleteModel(
            name='downvoteQuestion',
        ),
        migrations.DeleteModel(
            name='upvoteAnswer',
        ),
        migrations.DeleteModel(
            name='upvoteQuestion',
        ),
    ]
