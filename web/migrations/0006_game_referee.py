# Generated by Django 3.1.1 on 2021-02-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210216_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='referee',
            field=models.TextField(null=True),
        ),
    ]
