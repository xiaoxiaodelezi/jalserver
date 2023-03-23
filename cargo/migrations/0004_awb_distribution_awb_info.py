# Generated by Django 4.1.2 on 2022-12-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0003_suspicious_good'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awb_distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.CharField(max_length=3)),
                ('piece', models.IntegerField()),
                ('distribution_uuid', models.CharField(max_length=36)),
                ('distribution_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Awb_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12)),
                ('agent', models.CharField(max_length=3)),
                ('distribution_uuid', models.CharField(max_length=36)),
            ],
        ),
    ]