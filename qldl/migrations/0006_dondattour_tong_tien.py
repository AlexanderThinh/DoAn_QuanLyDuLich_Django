# Generated by Django 4.0.4 on 2022-04-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qldl', '0005_alter_like_unique_together_like_tin_tuc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dondattour',
            name='tong_tien',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
