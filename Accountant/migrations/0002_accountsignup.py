# Generated by Django 3.2.12 on 2023-01-24 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankInForm', '0003_newaccountform'),
        ('Accountant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSignUp',
            fields=[
                ('mybasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BankInForm.mybasemodel')),
                ('email_id', models.CharField(max_length=255)),
                ('create_password', models.IntegerField()),
                ('confirm_password', models.IntegerField()),
                ('forword_password', models.IntegerField()),
                ('user_signature', models.CharField(max_length=255)),
            ],
            bases=('BankInForm.mybasemodel',),
        ),
    ]
