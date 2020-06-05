# Generated by Django 3.0.6 on 2020-06-02 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceptances', '0003_auto_20200602_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptance',
            name='status',
            field=models.CharField(choices=[('WASH', 'Washed'), ('RECEIVED', 'Received'), ('TAKED', 'Takde')], default='RECEIVED', max_length=10),
        ),
    ]
