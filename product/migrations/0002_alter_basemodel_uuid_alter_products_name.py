# Generated by Django 5.0.4 on 2024-05-02 11:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=150),
        ),
    ]