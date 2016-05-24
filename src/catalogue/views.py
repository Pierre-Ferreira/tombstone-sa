from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from contactus.models import ContactUsInfo
from contactus.forms import ContactUsForm

# Create your views here.
def catalogue_view(request):
    form = ContactUsForm(request.POST or None)
    successMsg = ""
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, "Your request has been submitted!")
        return HttpResponseRedirect('/contactus')
    title = "Catalogue"
    nbar = "catalogue"
    context = {
        "form": form,
        "title": title,
        "nbar": nbar,
    }
    return render(request, 'catalogue_page.html', context)
