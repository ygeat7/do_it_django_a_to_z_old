# Generated by Django 4.1.3 on 2022-11-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
