# Generated by Django 5.1.5 on 2025-02-05 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_screening_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
