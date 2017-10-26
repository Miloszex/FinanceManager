# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Partner
from django.contrib.auth.models import User
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

def add_partner(request):

    if request.method == 'POST':
        searched_user = User.objects.get(username__startswith = request.POST['partner_name'])
        if searched_user:
            Partner.objects.create(subject=request.user, partner=searched_user)
            return render(request, 'board/partner_added.html')
        else:
            return render(request, 'board/partner_not_found.html')
    return render(request, 'board/search_partner.html')


def remove_partner(request, partner_id):
    pass
