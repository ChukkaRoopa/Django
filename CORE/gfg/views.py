from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import GeeksModel
from .forms import GeeksForm

# Create view
def CreateView(request):

    context = {}

    form = GeeksForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/list_view/')
    
    context['form'] = form

    return render(request, 'createview.html', context)


# Retrieve the content
# list view
def list_view(request):
    context = {"data": GeeksModel.objects.all(), "page": "list_view"}
    return render(request, "view_gfg.html", context)

# detailed view
def detailed_view(request, id):
    context = {'data': GeeksModel.objects.get(id = id), "page": "detailed_view"}
    return render(request, "detailed_view.html", context)

# Update view
def update_view(request, id):

    context = {}

    obj = get_object_or_404(GeeksModel, id = id)

    form = GeeksForm(request.POST or None, request.FILES or None, instance=obj)

    if form.is_valid():

        form.save() 
        return redirect('/list_view/') 
    
    context['form'] = form

    return render(request, "update_view.html", context)


# Delete view
def delete_view(request, id):

    context = {}

    obj = get_object_or_404(GeeksModel, id = id)

    if request.method == "POST":
        obj.delete()
        return redirect('/list_view/')
    
    return render(request, "delete_view.html", context)