# Generated by Django 4.1.4 on 2023-09-19 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="authhor",
            new_name="author",
        ),
    ]
