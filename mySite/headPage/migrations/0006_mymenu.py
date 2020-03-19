# Generated by Django 3.0.3 on 2020-03-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headPage', '0005_auto_20200227_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l1', models.DecimalField(decimal_places=0, max_digits=3)),
                ('l2', models.DecimalField(decimal_places=0, max_digits=3)),
                ('l3', models.DecimalField(decimal_places=0, max_digits=3)),
                ('l4', models.DecimalField(decimal_places=0, max_digits=3)),
                ('l5', models.DecimalField(decimal_places=0, max_digits=3)),
                ('first', models.BooleanField()),
                ('visible', models.BooleanField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'mymenu',
            },
        ),
    ]