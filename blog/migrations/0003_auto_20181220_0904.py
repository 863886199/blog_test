# Generated by Django 2.1.4 on 2018-12-20 01:04

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='boby',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excperpt',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
