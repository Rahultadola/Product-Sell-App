# Generated by Django 3.2.5 on 2021-08-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210806_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descrip_image',
            field=models.ImageField(null=True, upload_to='static/products'),
        ),
    ]
