# Generated by Django 5.1.4 on 2024-12-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="test",
            field=models.TextField(default="test text"),
            preserve_default=False,
        ),
    ]