# Generated by Django 2.1.7 on 2019-08-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190805_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='component',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
