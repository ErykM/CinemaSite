# Generated by Django 3.1.1 on 2020-12-20 17:48

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('ticket_prize', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', api.models.DecimalRangeField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
