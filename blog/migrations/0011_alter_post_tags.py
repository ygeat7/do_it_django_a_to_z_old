# Generated by Django 4.1.3 on 2022-12-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]