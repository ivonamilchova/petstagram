from django.shortcuts import render

def photo_add(request):
    return render(request, template_name='photos/photo-add-page.html')

def photo_details(request, pk:int):
    return render(request, template_name='photos/photo-details-page.html')

def photo_edit(request, pk:int):
    return render(request, template_name='photos/photo-edit-page.html')

