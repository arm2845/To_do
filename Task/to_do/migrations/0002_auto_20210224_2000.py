# Generated by Django 3.1.5 on 2021-02-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(default='Write description here.'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Doing'), (2, 'Done')], default=0),
        ),
    ]
