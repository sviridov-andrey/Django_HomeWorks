# Generated by Django 4.2.3 on 2023-11-20 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='verification',
        ),
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.BooleanField(default=False, verbose_name='верификация'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активность'),
        ),
    ]