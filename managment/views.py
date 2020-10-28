from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from .forms import PatientForm,TreatmentForm, HistoryForm

# Create your views here.
def home(request):
    return render(request, 'manag/home.html')

def Create(request):
    if request.method == 'GET':
        return render(request, 'manag/create.html',{'form':PatientForm})
    else:
        form = PatientForm(request.POST)
        nForm = form.save(commit=False)
        nForm.user = request.user
        nForm.save()
        return redirect('patient_view')

def patinet_form(request):
    if request.method =='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone =  request.POST.get('phone')
        email = request.POST.get('email')
        forms = Patient_info(name=name,age=age, address=address,phone=phone,email=email)
        forms.save()
        return render(request, 'manag/patient_view.html')
    else:
        return render(request, 'manag/patinet_form.html')

def patient_view(request):
    data = Treatment.objects.filter(user=request.user)
    pdata = Patient_info.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'manag/patient_view.html',{'form':TreatmentForm(),'trt':data,'data':pdata})
    else:
        tform = TreatmentForm(request.POST)
        ntform = tform.save(commit=False)
        ntform.user = request.user
        ntform.save()
        return render(request, 'manag/patient_view.html',{'form':TreatmentForm(),'trt':data,'pdata':pdata})    

def search(request):
    if request.method == 'POST':
        srch = request.POST['srch']
        if srch:
            match = Patient_info.objects.filter(Q(id__icontains = srch)|
                                               Q(name__icontains = srch)|
                                               Q(address__icontains = srch)
                                               )
            if match:
                return render(request,'manag/search.html', {'sr':match})
            else:
                messages.error(request,'no result found....!')
        else:
            return HttpRessponseRedirect('/search/')

    return render(request, 'manag/search.html')

def history(request):
    data = History.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'manag/history.html',{'form':HistoryForm(), 'data':data})
    else:
        tform = HistoryForm(request.POST)
        ntform = tform.save(commit=False)
        ntform.user = request.user
        ntform.save()
        data = History.objects.filter(user=request.user)
        return render(request,'manag/history.html',{'form':HistoryForm(), 'data':data})
