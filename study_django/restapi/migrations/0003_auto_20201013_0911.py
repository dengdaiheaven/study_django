# Generated by Django 3.1.2 on 2020-10-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20201013_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='cert_id',
            field=models.CharField(max_length=32),
        ),
    ]