from django.shortcuts import render, redirect

import bitcoinrpc
bitrpc = bitcoinrpc.connect_to_remote('bitcoin', 'lolhax')

def create(request):
  addr = bitrpc.getnewaddress( request.user.username )
  return render(request, 'wallet/create.html', { 'address':addr })

def index(request):
  addresses = bitrpc.getaddressesbyaccount( request.user.username )
  bal = bitrpc.getbalance( request.user.username )
  
  return render(request, 'wallet/index.html', {
    'wallets': addresses,
    'balance': ('%.2f' % bal)
  })

def send(request):
  # whatever
  return render(request, 'wallet/send.html')
