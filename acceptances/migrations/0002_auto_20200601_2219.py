# Generated by Django 3.0.6 on 2020-06-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptances', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptance',
            name='is_taked',
        ),
        migrations.RemoveField(
            model_name='acceptance',
            name='is_washed',
        ),
        migrations.AddField(
            model_name='acceptance',
            name='status',
            field=models.CharField(choices=[('WASH', 'Washed'), ('DONE', 'Done'), ('TAKED', 'Take')], default='WASH', max_length=10),
        ),
    ]
