# Generated by Django 3.2.23 on 2024-01-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20240129_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, verbose_name='Позиция фото'),
        ),
    ]
