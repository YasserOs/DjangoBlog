# Generated by Django 4.0.3 on 2022-03-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Awesome Blog!', max_length=255),
        ),
    ]