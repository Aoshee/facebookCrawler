from django.shortcuts import render
from django.http import *
from facebookData import *

def login(request):
    #app_id,redirect_url,scope are present appDetails.py
    url = "http://www.facebook.com/dialog/oauth/?client_id="+app_id+"&redirect_uri="+redirect_url+"&state=RANDOM_NUMBER&scope="+scope+"&response_type=code"
    return HttpResponseRedirect(url)

def getCode(request):
    code = request.GET.get('code')
    fb_obj = FbData()
    fb_obj.getAccessCode(code)
    return HttpResponse("Login Successful!! we are doing stuff at backend.")
