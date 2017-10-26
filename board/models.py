# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Wallet(models.Model):

    user = models.OneToOneField(User)
    actual_cash = models.FloatField(default=0)
    savings = models.FloatField(default=0)

    def __str__(self):
        return self.user.username + " wallet"

@receiver(post_save, sender=Wallet)
def createWalletLogger(sender, instance, created, **kwargs):
    if created:
        WalletLger.objects.create(wallet=instance.user.wallet)

class Partner(models.Model):

    subject = models.ForeignKey(User, related_name="wallet_owner")
    partner = models.ForeignKey(User, related_name="wallet_partner")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.subject.username + ' and ' + self.partner.username

class WalletLger(models.Model):

    wallet = models.ForeignKey(Wallet)

    def __str__(self):
        return self.wallet.user.username + " Wallet Logger "

class LgerMessage(models.Model):

    wallet = models.ForeignKey(WalletLger)
    message = models.CharField(max_length=200)
