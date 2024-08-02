from django.shortcuts import render,redirect
from dashboard.models import FormBarang
from django.contrib import messages

def tambah_barang(request):
    if request.POST:
    form= FormBarang(request.POST)
    if from.is_valid():
        from.save()
        messages.success(request,"")
    konteks={
        'form':form,
    }
    return render(request, 'tambah_barang.html',konteks)
else:
    form=FormBarang(
    konteks = {
        'form':form,
    }
return render(request, 'tambah_barang.html',konteks)
    )

def Barang_Views(request):
    barangs=Barang.objects.all()

    konteks={
        'barang':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def hapus_brg(request,id_barang):
    barang=Barang.objects.filter(id=id_barang)
    barangs.delete()
    message.success(request,"Data Terhapus")
    return redirect('Vbrg')