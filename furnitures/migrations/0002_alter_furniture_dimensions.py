# Generated by Django 3.2 on 2022-04-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='dimensions',
            field=models.CharField(max_length=254),
        ),
    ]