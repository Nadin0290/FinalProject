# Generated by Django 4.0.5 on 2022-06-21 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tube', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='authorSubscribed',
        ),
        migrations.AddField(
            model_name='video',
            name='videoHeader',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='video',
            name='videoTitle',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='video',
            name='videoViews',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribeChannel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tube.author')),
                ('subscribeUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]