# Generated by Django 4.2.16 on 2024-11-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
