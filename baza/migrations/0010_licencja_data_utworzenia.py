# Generated by Django 3.1.7 on 2021-04-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0009_remove_licencja_moduly'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencja',
            name='data_utworzenia',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
