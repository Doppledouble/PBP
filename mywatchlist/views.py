from django.shortcuts import render
from mywatchlist.models import BarangWatchlist
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist(request):
        data_movies_mywatchlist = BarangWatchlist.objects.all()
        context = {
        'Watched': data_movies_mywatchlist,
        'nama': 'Ian Suryadi Timothy H ',
        'npm' : '2106750875'
        }
        return render(request, "mywatchlist.html",context)
# Create your views here.
def show_xml(request):
    data = BarangWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = BarangWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    

def show_xml_by_id(request, id):
    data = BarangWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

