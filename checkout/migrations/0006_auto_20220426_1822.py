# Generated by Django 3.2 on 2022-04-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20220426_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_dolly',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]