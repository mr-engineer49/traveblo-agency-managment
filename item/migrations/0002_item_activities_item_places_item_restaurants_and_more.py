# Generated by Django 4.1.7 on 2023-05-26 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="activities",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="places",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="restaurants",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="trip",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="vacations",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="published_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
