# Generated by Django 3.2.5 on 2022-02-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_web_vitals', '0002_corewebvitals_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corewebvitals',
            name='url',
            field=models.URLField(),
        ),
    ]
