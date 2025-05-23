# Generated by Django 5.1.7 on 2025-05-23 08:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0002_remove_artikel_created_at_remove_artikel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artikel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
