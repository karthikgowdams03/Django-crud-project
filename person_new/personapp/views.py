from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, PersonForm

def person_list(request):
    #fetch all persons
    persons=Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons}) # send 'persons' list to the page

def person_create(request):
    if request.method == 'POST':
        # posted model form using person instance
        personForm = PersonForm(request.POST)
        # if valid form
        #   #i save
        #   #ii redirect to the list page
        #   return redirect('person_list_page') 
        if personForm.is_valid():
            personForm.save()
            return redirect('person_list_page') 
    else:
        # new model form 
        personForm = PersonForm()
        
    return render(request, 'person_create.html', {'personForm':personForm}) # pass form to the page

def person_edit(request, id):
    # get person instance from databse
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        # posted model form using person instance
        personForm = PersonForm(request.POST, instance=person)
        # if valid form
        #   # i save
        #   #ii redirect to the list page
        #   return redirect('person_list_page') 
        if personForm.is_valid():
            personForm.save()
            return redirect('person_list_page') 
    else:
        # new model form using person instance
        personForm = PersonForm(instance=person)
    return render(request, 'person_edit.html', {'personForm':personForm}) # pass form to the page        

def person_delete(request, id):
    # get person instance from databse 
    # delete the person in the db
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('person_list_page')  
