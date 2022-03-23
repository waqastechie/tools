# Generated by Django 3.2.5 on 2022-02-09 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'question_explorer_keywords',
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(max_length=1000)),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_explorer.keyword')),
            ],
            options={
                'db_table': 'question_explorer_suggestions',
            },
        ),
    ]
