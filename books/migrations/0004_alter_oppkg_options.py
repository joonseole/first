# Generated by Django 4.0.3 on 2022-07-24 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_networkfunction_nf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oppkg',
            options={'ordering': ['created_at'], 'verbose_name': 'Operator & Package'},
        ),
    ]
