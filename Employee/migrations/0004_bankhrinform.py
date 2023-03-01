# Generated by Django 3.2.12 on 2023-01-28 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankInForm', '0003_newaccountform'),
        ('Employee', '0003_auto_20230123_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankHRInform',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BankInForm.mybasemodel')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            bases=('BankInForm.mybasemodel',),
        ),
    ]