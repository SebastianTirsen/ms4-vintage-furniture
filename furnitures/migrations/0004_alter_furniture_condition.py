# Generated by Django 3.2 on 2022-04-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0003_alter_furniture_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='condition',
            field=models.CharField(blank=True, choices=[('1', 'Like New'), ('2', 'Good'), ('3', 'Worn')], max_length=300, null=True),
        ),
    ]
