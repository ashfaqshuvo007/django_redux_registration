# Generated by Django 3.0.2 on 2020-01-12 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_reg_redux', '0002_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dj_reg_redux.Branch'),
        ),
    ]
