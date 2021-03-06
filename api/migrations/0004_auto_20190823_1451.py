# Generated by Django 2.2.4 on 2019-08-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190823_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eolica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.FloatField()),
                ('w_s', models.FloatField()),
                ('w_d', models.CharField(max_length=20)),
                ('r', models.CharField(choices=[('ESTE', 'Este'), ('OESTE', 'Oeste'), ('NORTE', 'Norte'), ('SUR', 'Sur'), ('NOR ESTE', 'Nor este'), ('NOR OESTE', 'Nor oeste'), ('SUR OESTE', 'Sur oeste'), ('SUR ESTE', 'Sur este')], default='ESTE', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Generation',
        ),
    ]
