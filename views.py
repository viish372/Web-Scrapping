from django.shortcuts import render
from main import vish

import requests
import json
def index(request):
    return render(request, 'index.html')

def show(request):
    radio = request.POST['r1']
    dat = {'r1':radio}
    vish(radio)
    with open('data.json') as json_file:
         data = json.load(json_file)
    with open('data1.json') as json_file:
         data1 = json.load(json_file)
    with open('data2.json') as json_file:
         data2 = json.load(json_file)
    d = {
         "cc": data['contract_choice'],
         "e_dt": data['expiary_date'],
         "sp": data['Spot_price_nse'],
         "e_dt": data['expiary_date'],
         "calls_iv": data['IV_calls'],
         "nearest_Strike_P": data['nearest_strike_price'],
         "put_iv": data['IV_puts'],
         "large_put_oi": data['Largest_puts_oi'],
         "largest_puts_change_in_oi": data['Largest puts change in oi'],
         "largest_puts_volume": data['Largest puts volume'],
         "largest_calls_oi": data['Largest calls oi'],
         "largest_calls_change_in_oi": data['Largest calls change in oi'],
         "largest_calls_volume": data['Largest calls volume'],
         "Normal_dist_large_calls_oi": data['normal distribution for largest calls oi'],
         "Normal_dist_large_calls_change_in_oi": data['normal distribution for largest calls change in oi='],
         "Normal_dist_large_calls_volume": data['normal distribution for largest calls volume='],
         "Normal_dist_large_puts_oi": data['normal distribution for largest puts oi'],
         "Normal_dist_large_puts_change_in_oi": data['normal distribution for largest puts change in oi'],
         "Normal_dist_large_puts_volume": data['normal distribution for largest puts volume='],
         # Data for second Expiary
         "cc_d1": data1['contract_choice'],
         "e_dt_d1": data1['expiary_date'],
         "sp_d1": data1['Spot_price_nse'],
         "e_dt_d1": data1['expiary_date'],
         "calls_iv_d1": data1['IV_calls'],
         "nearest_Strike_P_d1": data1['nearest_strike_price'],
         "put_iv_d1": data1['IV_puts'],
         "large_put_oi_d1": data1['Largest_puts_oi'],
         "largest_puts_change_in_oi_d1": data1['Largest puts change in oi'],
         "largest_puts_volume_d1": data1['Largest puts volume'],
         "largest_calls_oi_d1": data1['Largest calls oi'],
         "largest_calls_change_in_oi_d1": data1['Largest calls change in oi'],
         "largest_calls_volume_d1": data1['Largest calls volume'],
         "Normal_dist_large_calls_oi_d1": data1['normal distribution for largest calls oi'],
         "Normal_dist_large_calls_change_in_oi_d1": data1['normal distribution for largest calls change in oi='],
         "Normal_dist_large_calls_volume_d1": data1['normal distribution for largest calls volume='],
         "Normal_dist_large_puts_oi_d1": data1['normal distribution for largest puts oi'],
         "Normal_dist_large_puts_change_in_oi_d1": data1['normal distribution for largest puts change in oi'],
         "Normal_dist_large_puts_volume_d1": data1['normal distribution for largest puts volume='],
         # Data for Third Expiary
         "cc_d2": data2['contract_choice'],
         "e_dt_d2": data2['expiary_date'],
         "sp_d2": data2['Spot_price_nse'],
         "e_dt_d2": data2['expiary_date'],
         "calls_iv_d2": data2['IV_calls'],
         "nearest_Strike_P_d2": data2['nearest_strike_price'],
         "put_iv_d2": data2['IV_puts'],
         "large_put_oi_d2": data2['Largest_puts_oi'],
         "largest_puts_change_in_oi_d2": data2['Largest puts change in oi'],
         "largest_puts_volume_d2": data2['Largest puts volume'],
         "largest_calls_oi_d2": data2['Largest calls oi'],
         "largest_calls_change_in_oi_d2": data2['Largest calls change in oi'],
         "largest_calls_volume_d2": data2['Largest calls volume'],
         "Normal_dist_large_calls_oi_d2": data2['normal distribution for largest calls oi'],
         "Normal_dist_large_calls_change_in_oi_d2": data2['normal distribution for largest calls change in oi='],
         "Normal_dist_large_calls_volume_d2": data2['normal distribution for largest calls volume='],
         "Normal_dist_large_puts_oi_d2": data2['normal distribution for largest puts oi'],
         "Normal_dist_large_puts_change_in_oi_d2": data2['normal distribution for largest puts change in oi'],
         "Normal_dist_large_puts_volume_d2": data2['normal distribution for largest puts volume=']

    }
    return render(request, 'second.html',d)


#def second(request):

 #   return render(request, 'second.html',d)

