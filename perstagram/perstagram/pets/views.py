from django.shortcuts import render

def pet_details(request, username:str, pet_slug:str):
    return render(request, template_name='pets/pet-details-page.html')

def pet_add(request, username:str, pet_slug:str):
    
    return render(request, template_name='pets/pet-add-page.html')

def pet_edit(request, username:str, pet_slug:str):
    return render(request, template_name='pets/pet-edit-page.html')

def pet_delete(request, username:str, pet_slug:str):
    return render(request, template_name='pets/pet-delete-page.html')

