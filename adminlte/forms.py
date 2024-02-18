from django import forms
from .models import PersonalInformation


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Father's Name"}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mother's Name"}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "YYYY-MM-DD"}), 
            'gender': forms.Select(attrs={'class': 'form-control'}),

            'name_of_degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Degree'}),
            'admission_session': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission Session'}),
            'reg_id_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reg/ID No.'}),
            'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch'}),
            'year_of_passing': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year of Passing'}),
            'graduating_session': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Graduating Session'}),
            'cgpa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CGPA'}),

            'name_of_degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Degree'}),
            'admission_session': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admission Session'}),
            'reg_id_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reg/ID No.'}),
            'batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch'}),
            'year_of_passing': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year of Passing'}),
            'graduating_session': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Graduating Session'}),
            'cgpa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CGPA'}),
        }
