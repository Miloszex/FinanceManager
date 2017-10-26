# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Wallet, Partner, WalletLger, LgerMessage
# Register your models here.

admin.site.register(Wallet)
admin.site.register(Partner)
admin.site.register(WalletLger)
admin.site.register(LgerMessage)
