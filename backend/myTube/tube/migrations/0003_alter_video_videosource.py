# Generated by Django 4.0.5 on 2022-06-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_remove_author_authorsubscribed_video_videoheader_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videoSource',
            field=models.FileField(upload_to='videos'),
        ),
    ]