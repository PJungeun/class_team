# Generated by Django 2.1.7 on 2019-08-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='writer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]