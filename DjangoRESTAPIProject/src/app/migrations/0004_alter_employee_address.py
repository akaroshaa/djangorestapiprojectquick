# Generated by Django 4.0.4 on 2022-05-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]