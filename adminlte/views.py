from django.shortcuts import render , redirect
from .forms import PersonalInformationForm
from .models import PersonalInformation

# Create your views here.

def home(request) :
    return render(request , 'adminlte/index.html')

def form(request) :
    # draft_instance = PersonalInformation.objects.filter(user=request.user, is_submitted=False).first()

    # if request.method == 'POST':
    #     form = PersonalInformationForm(request.POST, instance=draft_instance)
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         action = request.POST.get('action')
    #         if action == 'draft':
    #             form.instance.is_submitted = False
    #             form.save()  # Save the draft
    #             print('Draft saved:', form.cleaned_data)
    #             return redirect('form')  # Redirect to the form page
    #         elif action == 'confirm':
    #             form.instance.is_submitted = True
    #             form.save()  # Save the submitted form
    #             print('Form submitted:', form.cleaned_data)
    #             # Disable draft saving after confirmation
    #             return redirect('form')  # Redirect to the form page
    # else:
    #     if draft_instance:
    #         form = PersonalInformationForm(instance=draft_instance)
    #     else:
    #         form = PersonalInformationForm()

    # return render(request, 'adminlte/pages/forms/myform.html', {'form': form})

    form = PersonalInformationForm(request.POST)
    if form.is_valid() : 
        form.save()
        print(form.cleaned_data)
    else : 
        print('form is not ok')
    return render(request, 'adminlte/pages/forms/myform.html' , {'form':form})


def base(request) : 
    return render(request, 'base.html')