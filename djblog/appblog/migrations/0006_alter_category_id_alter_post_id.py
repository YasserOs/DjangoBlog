# Generated by Django 4.0.3 on 2022-03-18 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0005_auto_20220318_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
