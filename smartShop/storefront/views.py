# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404,HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
from storefront.models import Store,StoreAdmin 


def home(request):
	return HttpResponse("U have been redirected to the home page - Hello World!")

def index(request):
	return home(request)
