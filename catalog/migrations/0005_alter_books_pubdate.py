# Generated by Django 4.1.3 on 2022-11-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_books_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pubdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
