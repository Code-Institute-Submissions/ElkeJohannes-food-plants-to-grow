# Generated by Django 4.0 on 2022-02-17 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('suggestions', '0002_remove_suggestion_user_suggestion_upvoters'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.useraccount'),
        ),
    ]