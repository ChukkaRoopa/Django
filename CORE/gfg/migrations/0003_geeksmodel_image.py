# Generated by Django 4.2.16 on 2024-12-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfg', '0002_rename_geeks_geeksmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gfg'),
        ),
    ]
