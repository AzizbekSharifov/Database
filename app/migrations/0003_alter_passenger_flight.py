# Generated by Django 5.1.3 on 2024-12-03 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_passenger_first_name_alter_passenger_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='app.flight'),
        ),
    ]
