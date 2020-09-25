from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Std_profile
from .forms import Std_profileForm
# Create your views here.
def std_list(request) :
    std_list = Std_profile.objects.all()
    context = {'std_list':std_list}
    return render(request, 'Profile.html', context)

def std_detail(request, pk):
    std_detail = Std_profile.objects.get(pk=pk)
    context = {'std_detail' : std_detail}
    return render(request, 'details_std.html' , context)
    

def edit(request,pk):
    edit =Std_profile.objects.get(pk=pk)
    if request.method == 'POST' :
        form = Std_profileForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = Std_profileForm(instance=edit)
        return render(request, 'edit.html', {'form' : form,})

def std_delete(request , pk):
    std_delete = Std_profile.objects.get(pk=pk)
    std_delete.delete()
    return redirect('home:std_list')