# Generated by Django 2.0.2 on 2018-03-02 14:58

from django.db import migrations, models
import django.db.models.deletion


def get_some_int():
    from django.utils import timezone
    return timezone.now().time().microsecond

class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='brnd',
            field=models.ForeignKey(default=get_some_int, on_delete=django.db.models.deletion.CASCADE, to='demoapp.Brands'),
            preserve_default=False,
        ),
    ]
