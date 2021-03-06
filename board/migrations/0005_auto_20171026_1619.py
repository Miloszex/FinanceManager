# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20171026_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='LgerMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='walletlger',
            name='message',
        ),
        migrations.AddField(
            model_name='lgermessage',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.WalletLger'),
        ),
    ]
