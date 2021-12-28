# Generated by Django 4.0 on 2021-12-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_alter_plant_layer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='Layer',
            field=models.CharField(choices=[('Large trees', 'Large trees'), ('Medium trees', 'Medium trees'), ('Small trees', 'Small trees'), ('Shrubs', 'Shrubs'), ('Ground covers', 'Ground covers'), ('Climbers', 'Climbers'), ('Roots', 'Roots')], max_length=100),
        ),
    ]
