# Generated by Django 4.0.4 on 2022-04-18 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qldl', '0003_tour_thoi_gian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dondattour',
            name='loai_ve',
        ),
        migrations.AddField(
            model_name='dondattour',
            name='loai_ve',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dondattour', to='qldl.loaive'),
        ),
    ]
