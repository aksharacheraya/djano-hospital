# Generated by Django 4.1 on 2023-01-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discription', models.TextField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
