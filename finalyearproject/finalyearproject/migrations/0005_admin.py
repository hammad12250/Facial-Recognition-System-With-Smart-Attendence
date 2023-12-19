# Generated by Django 4.2.4 on 2023-12-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalyearproject', '0004_alter_employee_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('admin_id', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]