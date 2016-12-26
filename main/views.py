from django.shortcuts import render
from django.http import HttpResponse

import time
import os
from django.conf import settings
import cStringIO
import sys



import base64
import json
import requests

from base64 import b64encode




def imguruploader(request):
	#try:
	a = request.POST
	print a
	client_id = 'ad3002cdda698d8'

	headers = {"Authorization": "Client-ID %s"%(client_id)}

	url = "https://api.imgur.com/3/upload.json"
	#file = cStringIO.StringIO(base64.b64decode(request.FILES['file1']))
	api_key = '37ee388bf32de161bb82e3852124c0af4ae40f19'

	url = "https://api.imgur.com/3/upload.json"

	j1 = requests.post(
	    url, 
	    headers = headers,
	    data = {
	        'key': api_key, 
	        'image': a,
	        'type': 'base64',
	        'name': '1.jpg',
	        'title': 'Picture no. 1'
	    }
	)
	print j1
	print "naha chala bhai"
		#return HttpResponse(j1.text)
	#except Exception as e:
		#print e
		#print "there was an exception"

	return HttpResponse("hey there")

	



def index(request):
	return render(request,'main/upload.html')