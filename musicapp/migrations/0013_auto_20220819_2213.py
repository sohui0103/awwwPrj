# Generated by Django 3.0.8 on 2022-08-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0012_remove_blog_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blog',
        ),
    ]
