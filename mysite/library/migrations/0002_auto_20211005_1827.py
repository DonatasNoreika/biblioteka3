# Generated by Django 3.2.7 on 2021-10-05 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Autorius', 'verbose_name_plural': 'Autoriai'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Knyga', 'verbose_name_plural': 'Knygos'},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'verbose_name': 'Knygos egzempliorius', 'verbose_name_plural': 'Knygų egzemplioriai'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Žanras', 'verbose_name_plural': 'Žanrai'},
        ),
    ]
