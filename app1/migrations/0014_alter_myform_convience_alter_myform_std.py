# Generated by Django 4.1.1 on 2022-09-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_myform_convience_alter_myform_std'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myform',
            name='Convience',
            field=models.CharField(choices=[('Bus', 'Bus'), ('None', 'None'), ('Liberary', 'Liberary'), ('Both', 'Both')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myform',
            name='Std',
            field=models.CharField(choices=[('iv', 'iv'), ('v', 'v'), ('ix', 'ix'), ('i', 'i'), ('x', 'x'), ('vi', 'vi'), ('viii', 'viii'), ('ii', 'ii'), ('iii', 'iii'), ('vii', 'vii')], max_length=50, null=True),
        ),
    ]