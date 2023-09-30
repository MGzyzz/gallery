# Generated by Django 4.2.5 on 2023-09-30 09:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user_favorite',
            field=models.ManyToManyField(blank=True, related_name='like_publications', to=settings.AUTH_USER_MODEL),
        ),
    ]