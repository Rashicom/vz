# Generated by Django 5.0.4 on 2024-05-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comboproducts',
            name='free_bottles',
            field=models.ManyToManyField(blank=True, null=True, related_name='included_free_bottles_combo', to='product.productbottles'),
        ),
    ]
