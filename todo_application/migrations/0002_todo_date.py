# Generated by Django 4.1.4 on 2023-04-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_application", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="date",
            field=models.DateField(default="1999-03-11"),
            preserve_default=False,
        ),
    ]
