# Generated by Django 4.2.3 on 2023-11-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_verification_code_auto_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='verification_code_auto',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verification_code_user',
        ),
        migrations.AddField(
            model_name='user',
            name='verification',
            field=models.BooleanField(default=False, verbose_name='Верификация'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
    ]