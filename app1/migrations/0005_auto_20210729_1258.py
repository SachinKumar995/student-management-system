# Generated by Django 3.2 on 2021-07-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20210729_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='Convience',
            field=models.CharField(choices=[('Bus', 'Bus'), ('Liberary', 'Liberary'), ('Both', 'Both'), ('None', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myform',
            name='Std',
            field=models.CharField(choices=[('ii', 'ii'), ('vi', 'vi'), ('vii', 'vii'), ('ix', 'ix'), ('iii', 'iii'), ('v', 'v'), ('viii', 'viii'), ('iv', 'iv'), ('x', 'x'), ('i', 'i')], max_length=50, null=True),
        ),
    ]