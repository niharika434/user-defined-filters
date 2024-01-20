from django.shortcuts import render

# Create your views here.
def userfilter(request):
    d={'data':'Hi It is Me, BoNoboNoya'}
    return render(request,'userfilter.html',d)
