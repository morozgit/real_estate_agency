# Generated by Django 2.2.24 on 2023-09-05 17:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230905_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_flat',
            new_name='flat',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
