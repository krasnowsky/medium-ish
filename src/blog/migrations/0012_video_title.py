# Generated by Django 4.0.5 on 2022-06-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_options_alter_video_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
