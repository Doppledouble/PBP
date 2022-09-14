from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_catalog(request):
        data_barang_Catalog = CatalogItem.objects.all()
        context = {
        'list_barang': data_barang_Catalog,
        'nama': 'Ian Suryadi Timothy H ',
        'npm' : '2106750875'
        }
        return render(request, "katalog.html",context)