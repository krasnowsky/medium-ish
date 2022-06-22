# Generated by Django 4.0.5 on 2022-06-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={},
        ),
        migrations.RemoveField(
            model_name='video',
            name='added',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='videos',
            field=models.ManyToManyField(to='blog.video'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
