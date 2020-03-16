# Generated by Django 3.0.4 on 2020-03-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200315_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Характеристик')),
                ('text', models.CharField(max_length=150, verbose_name='Значение')),
                ('product', models.ManyToManyField(blank=True, to='shop.Product')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
    ]
