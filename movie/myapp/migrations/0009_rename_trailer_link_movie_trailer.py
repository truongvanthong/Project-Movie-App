# Generated by Django 4.2 on 2023-04-22 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_remove_movie_trailor_movie_trailer_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie", old_name="trailer_link", new_name="trailer",
        ),
    ]