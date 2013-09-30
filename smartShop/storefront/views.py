# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render,redirect,render_to_response
from storefront.models import Store,StoreAdmin 
from storefront.api import StoreResource



def home(request):
#	return HttpResponse("U have been redirected to the home page - Hello World!")
    res = StoreResource()
    request_bundle = res.build_bundle(request=request)
    queryset = res.obj_get_list(request_bundle)

    bundles = []
    for obj in queryset:
        bundle = res.build_bundle(obj=obj, request=request)
        bundles.append(res.full_dehydrate(bundle, for_list=True))

    list_json = res.serialize(None, bundles, "application/json")

    return HttpResponse(list_json)

    return render(request,'storefront/login.html')

def login(request):

    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        if not email  or not password: 
            return HttpResponse("Please enter the Details")
        try:
             userDetails = StoreAdmin.objects.get(admin_email = email)
        except StoreAdmin.DoesNotExist:
            return HttpResponse("User doesnot exist")
        if userDetails.admin_password == password:
            #request.session['uid'] = userDetails.id
            return redirect('/api/v1/store/1/?format=json')

        return HttpResponse("Enter the Details")
    return render(request,'storefront/login.html')

	

def register(request):
    if request.method=='POST':        
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
    return render(request,'storefront/register.html')
	

def index(request):
    return home(request)
