# Generated by Django 3.2.12 on 2023-01-24 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankInForm', '0003_newaccountform'),
        ('Accountant', '0004_auto_20230124_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteAccount',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BankInForm.mybasemodel')),
                ('name', models.CharField(max_length=255)),
                ('account_no', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            bases=('BankInForm.mybasemodel',),
        ),
    ]
