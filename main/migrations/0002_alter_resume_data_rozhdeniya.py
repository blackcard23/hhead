# Generated by Django 5.1 on 2024-08-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='data_rozhdeniya',
            field=models.IntegerField(verbose_name='Data Rozhdeniya'),
        ),
    ]
