# Generated by Django 3.2 on 2022-04-20 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0006_alter_furniture_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
