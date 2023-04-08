# Generated by Django 4.2 on 2023-04-08 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
                ('relev', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('publicationMoment', models.DateTimeField(auto_now=True)),
                ('tag', models.ManyToManyField(related_name='tgs', to='website.tag')),
            ],
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(max_length=500)),
                ('rating', models.IntegerField()),
                ('isRight', models.BooleanField()),
                ('authorId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.user')),
                ('questionId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.question')),
            ],
        ),
    ]
