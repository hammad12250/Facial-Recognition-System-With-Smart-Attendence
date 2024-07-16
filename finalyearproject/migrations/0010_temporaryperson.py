# Generated by Django 4.2.4 on 2024-03-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalyearproject', '0009_guard'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('person_id', models.CharField(max_length=10)),
                ('reason_for_visiting', models.TextField()),
                ('expiration_datetime', models.DateTimeField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]