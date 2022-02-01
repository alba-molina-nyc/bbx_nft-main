# Generated by Django 4.0.1 on 2022-02-01 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_nft_app', '0006_remove_item_user_delete_collection_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('details_url', models.URLField()),
                ('description', models.TextField()),
                ('properties', models.CharField(max_length=100)),
                ('levels', models.CharField(max_length=100)),
                ('stats', models.CharField(max_length=100)),
                ('unlockable_content', models.BooleanField(default=False)),
                ('explicit_or_sensitive_content', models.BooleanField(default=False)),
                ('supply', models.IntegerField(default=1)),
                ('blockchain', models.CharField(choices=[('E', 'Ethereum'), ('P', 'Polygon')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_choice_text', models.CharField(max_length=200)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_nft_app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]