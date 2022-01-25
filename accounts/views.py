from django.shortcuts import render,HttpResponse
from .forms import  AuthorForm
from.models import*

def home(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/thanks')

        else:
            return('Wrong values')
            
    form = AuthorForm()
    context={
        'form':form,
    }
    return render(request,'accounts/home.html',context)

    #return HttpResponse(('My home'))