# Generated by Django 3.2.6 on 2021-09-26 10:28

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210914_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailor',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
