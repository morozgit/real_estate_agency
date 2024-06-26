# Generated by Django 2.2.24 on 2023-08-31 12:04

from django.db import migrations
import phonenumbers


def set_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        try:
            phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(phonenumber):
                flat.owner_pure_phone = phonenumber
            else:
                flat.owner_pure_phone = None
        except (phonenumbers.NumberParseException, AttributeError):
            continue
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(set_phone_number)
    ]
