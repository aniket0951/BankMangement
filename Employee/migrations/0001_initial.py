# Generated by Django 3.2.12 on 2023-01-22 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BankInForm', '0003_newaccountform'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpolyeeInformation',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BankInForm.mybasemodel')),
                ('no_emp', models.IntegerField()),
                ('branch', models.CharField(max_length=155)),
                ('payment', models.IntegerField()),
                ('department', models.CharField(max_length=155)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
            ],
            bases=('BankInForm.mybasemodel',),
        ),
    ]