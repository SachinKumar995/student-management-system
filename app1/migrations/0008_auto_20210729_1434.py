# Generated by Django 3.2 on 2021-07-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210729_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='Convience',
            field=models.CharField(choices=[('Liberary', 'Liberary'), ('None', 'None'), ('Bus', 'Bus'), ('Both', 'Both')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myform',
            name='Std',
            field=models.CharField(choices=[('ix', 'ix'), ('v', 'v'), ('vii', 'vii'), ('viii', 'viii'), ('iii', 'iii'), ('x', 'x'), ('iv', 'iv'), ('i', 'i'), ('ii', 'ii'), ('vi', 'vi')], max_length=50, null=True),
        ),
    ]