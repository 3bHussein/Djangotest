# Generated by Django 4.0.1 on 2022-01-30 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='statius',
            new_name='status',
        ),
    ]
