# Generated by Django 4.0.1 on 2022-01-26 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_nft_app', '0004_rename_item_collection_collection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='collection',
            new_name='item',
        ),
    ]
