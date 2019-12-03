# Generated by Django 3.0 on 2019-12-03 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='药物名')),
                ('in_price', models.FloatField(verbose_name='进货价')),
                ('price', models.FloatField(verbose_name='单价')),
                ('count', models.IntegerField(verbose_name='库存数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '药物',
                'verbose_name_plural': '药物',
                'db_table': 'medicine',
            },
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='类型名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='修改时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_medicine_types', to=settings.AUTH_USER_MODEL, verbose_name='创建者id')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_medicine_types', to=settings.AUTH_USER_MODEL, verbose_name='修改者id')),
            ],
            options={
                'verbose_name': '药物类型',
                'verbose_name_plural': '药物类型',
                'db_table': 'medicine_type',
            },
        ),
        migrations.CreateModel(
            name='MedicineHandoutRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_medicine_handout_records', to=settings.AUTH_USER_MODEL, verbose_name='创建者id')),
            ],
            options={
                'verbose_name': '药物发放记录',
                'verbose_name_plural': '药物发放记录',
                'db_table': 'medicine_handout_record',
            },
        ),
    ]
