# Generated by Django 3.0.3 on 2020-02-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0005_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='money',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='amount',
            name='userId',
            field=models.BigIntegerField(),
        ),
    ]
