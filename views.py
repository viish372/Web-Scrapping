from django.shortcuts import render
import requests
import json

from access import access2


def index(request):
    return render(request, 'request.html')
def show(request):
    r_t = request.POST['request1']
    pnl = request.POST['pnl']
    access2(r_t,pnl)
    return render(request,'success.html')
