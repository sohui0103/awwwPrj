# Generated by Django 3.0.8 on 2022-08-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0008_delete_userplaylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
