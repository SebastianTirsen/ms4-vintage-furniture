# Generated by Django 3.2 on 2022-04-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_orderlineitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
