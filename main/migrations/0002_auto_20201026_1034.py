# Generated by Django 3.1.2 on 2020-10-26 00:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField(null=True, verbose_name='Дата')),
                ('printed_count', models.IntegerField(null=True, verbose_name='Количество отпечатанных страниц')),
                ('black_cart_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование черного картриджа')),
                ('black_tonerlevel', models.IntegerField(blank=True, null=True, verbose_name='Уровень черного тонера')),
                ('cyan_cart_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование голубого картриджа')),
                ('cyan_tonerlevel', models.IntegerField(blank=True, null=True, verbose_name='Уровень голубого тонера')),
                ('mag_cart_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование малинового картриджа')),
                ('mag_tonerlevel', models.IntegerField(blank=True, null=True, verbose_name='Уровень малинового тонера')),
                ('yel_cart_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование желтого картриджа')),
                ('yel_tonerlevel', models.IntegerField(blank=True, null=True, verbose_name='Уровень желтого тонера')),
            ],
        ),
        migrations.AlterField(
            model_name='device',
            name='inv_num',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{15}$')], verbose_name='Инвентарный номер'),
        ),
        migrations.AlterField(
            model_name='device',
            name='update_date',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
        migrations.DeleteModel(
            name='DeviceStat',
        ),
        migrations.AddField(
            model_name='devicedetail',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.device'),
        ),
    ]
