# Generated by Django 3.0.7 on 2020-06-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0003_ratings_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='Rate',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='Text',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
