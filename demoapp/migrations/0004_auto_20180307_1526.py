# Generated by Django 2.0.2 on 2018-03-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_auto_20180307_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='col',
            field=models.ManyToManyField(related_name='cars', to='demoapp.Colors'),
        ),
    ]
