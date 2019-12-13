# Generated by Django 3.0 on 2019-12-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='filter',
            name='string data or num data not null',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='number_data',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='string_data',
        ),
        migrations.AddField(
            model_name='filter',
            name='compare_option',
            field=models.CharField(choices=[('exactly', 'exactly'), ('between', 'between'), ('more', 'more than'), ('less', 'less than'), ('enum', 'enum')], default='exactly', max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filter',
            name='number',
            field=models.DecimalField(decimal_places=4, default=0.2, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filter',
            name='range',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True),
        ),
        migrations.DeleteModel(
            name='NumberData',
        ),
        migrations.DeleteModel(
            name='StringData',
        ),
    ]