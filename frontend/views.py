from django.http import HttpResponse
from functions import conn_varnish
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def index_view(request):
    return render_to_response('frontend/index.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def status_view(request):
    pass

@login_required
def portal_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('frontend/index.html')
