# Generated by Django 5.2.1 on 2025-06-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopsi', '0003_alter_hewan_options_alter_pengajuanadopsi_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hewan',
            name='jenis',
            field=models.CharField(choices=[('kucing', 'Kucing'), ('anjing', 'Anjing'), ('kelinci', 'Kelinci'), ('hamster', 'Hamster'), ('iguana', 'Iguana'), ('landak', 'Landak')], max_length=10),
        ),
    ]
