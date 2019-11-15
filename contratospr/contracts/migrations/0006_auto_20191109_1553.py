# Generated by Django 2.2.6 on 2019-11-09 15:53

from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("contracts", "0005_auto_20190825_1958")]

    operations = [
        UnaccentExtension(),
        migrations.RunSQL(
            "CREATE TEXT SEARCH CONFIGURATION spanish_unaccent(COPY=spanish);",
            "ALTER TEXT SEARCH CONFIGURATION spanish_unaccent ALTER MAPPING FOR hword, hword_part, word WITH unaccent, spanish_stem;",
        ),
    ]
