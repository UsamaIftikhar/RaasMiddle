# Generated by Django 2.1.15 on 2020-07-12 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200707_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='APP',
            fields=[
                ('app_id', models.UUIDField(primary_key=True, serialize=False)),
                ('appname', models.CharField(max_length=15)),
                ('webaddress', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('company_id', models.UUIDField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.company'),
        ),
    ]
