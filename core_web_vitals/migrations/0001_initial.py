# Generated by Django 3.2.5 on 2022-02-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreWebVitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('lcp', models.FloatField(null=True)),
                ('fcp', models.FloatField(null=True)),
                ('si', models.FloatField(null=True)),
                ('tti', models.FloatField(null=True)),
                ('tbt', models.FloatField(null=True)),
                ('score', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_web_vitals',
            },
        ),
    ]
