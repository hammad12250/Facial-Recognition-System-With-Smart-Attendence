# Generated by Django 4.2.2 on 2023-12-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalyearproject', '0003_alter_employee_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
