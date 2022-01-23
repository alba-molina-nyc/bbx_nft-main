# Generated by Django 3.2.9 on 2022-01-12 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('details_link', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('collection', models.CharField(max_length=250)),
                ('properties', models.CharField(max_length=100)),
                ('levels', models.CharField(max_length=100)),
                ('stats', models.CharField(max_length=100)),
                ('unlockable_content', models.BooleanField(default=False)),
                ('explicit_or_sensitive_content', models.BooleanField(default=False)),
                ('supply', models.IntegerField(default=1)),
                ('blockchain', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
