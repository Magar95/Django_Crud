# Generated by Django 5.1.1 on 2024-09-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
