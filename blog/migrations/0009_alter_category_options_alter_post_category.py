# Generated by Django 4.1.3 on 2022-12-01 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_category_post_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category", options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blog.category",
            ),
        ),
    ]
