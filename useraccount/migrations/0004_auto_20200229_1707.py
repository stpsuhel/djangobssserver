# Generated by Django 3.0.3 on 2020-02-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_auto_20200229_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
