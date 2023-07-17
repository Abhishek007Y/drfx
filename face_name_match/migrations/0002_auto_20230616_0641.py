# Generated by Django 3.1.2 on 2023-06-16 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('face_name_match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facematching',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
