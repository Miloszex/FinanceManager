# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/account/signin/")
def index(request):
    return render(request, 'board/board.html')

def wallet(request):
    pass

def wallet_payment(request):
    pass

def wallet_withraw(request):
    pass

def history(request):
    pass

def history_details(request, id):
    pass

def partners(request):
    pass

def add_partner(request, partner_name):
    pass

def remove_partner(request, partner_id):
    pass
    