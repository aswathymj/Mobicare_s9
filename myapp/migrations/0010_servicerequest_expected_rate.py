# Generated by Django 5.0.6 on 2024-09-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_complaint_expected_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='expected_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
