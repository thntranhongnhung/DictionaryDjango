# Generated by Django 4.1.4 on 2022-12-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='example',
            field=models.CharField(max_length=255, null=True),
        ),
    ]