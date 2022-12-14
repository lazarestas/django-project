# Generated by Django 4.1.3 on 2022-11-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_language_language_name_language_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(default='Russian', help_text='Enter a book language', max_length=20),
        ),
    ]
