# Generated by Django 3.2.3 on 2021-06-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20210526_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.TextField(null=True),
        ),
    ]
