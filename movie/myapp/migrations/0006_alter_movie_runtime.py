# Generated by Django 4.2 on 2023-04-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_remove_movie_budget_remove_movie_revenue_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="runtime",
            field=models.CharField(max_length=100, null=True),
        ),
    ]