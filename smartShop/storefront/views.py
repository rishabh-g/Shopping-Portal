# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
from storefront.models import Store,StoreAdmin 


def home(request):
#	return HttpResponse("U have been redirected to the home page - Hello World!")
    if 'email' in request.session:
        return render(request,'storefront/login.html')
    else:
        return render(request,'storefront/login.html')

def login(request):
    print str(request.POST)
    email = request.POST['email']
    password = request.POST['password']
    print type(email)
    print "\n"
    if(not email  or not password ): 
        return HttpResponse("Enter the Details")
    try:
         userDetails = StoreAdmin.objects.get(admin_email = email)
         print str(userDetails)
    except StoreAdmin.DoesNotExist:
        return HttpResponse("User doesnot exist")
    print str(userDetails)
    if userDetails.admin_password == password:
        request.session['uid'] = userDetails.id
        return HttpResponse("Login Successful")

    return HttpResponse("Enter the Details")
	

def register(request):
    store_name=request.POST['store_name']
    store_address=request.POST['store_address']
    store_phone=request.POST['store_phone']
    store_website=request.POST['store_website']
    store_email=request.POST['store_email']
    store_hours=request.POST['store_hours']

    store=Store(store_name=store_name,store_address=store_address,store_phone=store_phone,store_website=store_website,store_email=store_email,store_hours=store_hours)
    store.save()
    admin_email=request.POST['admin_email']
    admin_password=request.POST['admin_password']
    admin_storeid=store
    storead=StoreAdmin(admin_email=admin_email,admin_password=admin_password,admin_storeid=admin_storeid)
    storead.save()
    request.session['email']=admin_email
    return home(request)
	

def index(request):
    return home(request)
