# Generated by Django 4.2.5 on 2023-09-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_competition_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='last_updated',
            field=models.TextField(null=True),
        ),
    ]
