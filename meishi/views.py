from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from meishi.models import Meishi

@login_required
def index(request):
    u = request.user
    return render_to_response('meishi/index.html', {'user': u},
            context_instance=RequestContext(request))

@permission_required('meishi.add_company')
def list_user(request):
    c = request.user.get_profile().company
    u = User.objects.filter(userprofile__company__id = c.id)
    return render_to_response('meishi/list_user.html', {'user_list': u, 'company': c},
            context_instance=RequestContext(request))

@permission_required('meishi.add_company')
def company_information(request):
    c = request.user.get_profile().company
    return render_to_response('meishi/company_information.html', {'company': c},
            context_instance=RequestContext(request))

def exchange(request):
    return HttpResponse("unimplemented")

def exchange_history(request):
    return HttpResponse("unimplemented")

@login_required
def meishi_detail(request, meishi_id):
    m = get_object_or_404(Meishi, pk=meishi_id)
    return render_to_response('meishi/detail.html', {'meishi': m},
            context_instance=RequestContext(request))

@login_required
def meishi_add(request):
    return HttpResponse("unimplemented")

@login_required
def my_meishi(request):
    m = request.user.get_profile().meishi
    return render_to_response('meishi/my_meishi.html', {'meishi': m},
            context_instance=RequestContext(request))

@login_required
def my_meishi_json(request):
    m = request.user.get_profile().meishi
    jm = serializers.serialize("json", [m], ensure_ascii=False)
    return HttpResponse(jm, mimetype="application/json")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
