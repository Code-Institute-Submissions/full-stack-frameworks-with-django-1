# Generated by Django 2.2.4 on 2019-12-17 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20191217_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(blank=True, choices=[('CRITICAL', 'Critical'), ('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default='LOW', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('FR', 'Funding Required'), ('IP', 'In Progress'), ('C', 'Completed')], default='IP', max_length=2),
        ),
    ]