# Generated by Django 3.2.5 on 2022-02-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_keyword_researcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]