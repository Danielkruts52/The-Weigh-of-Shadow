from django import forms
from .models import DisabilityVacancy, Vacancy, YoungVacancy, Investor, cooperation, Space

class DisabilityVacancyForm(forms.ModelForm):
    class Meta:
        model = DisabilityVacancy
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter your first and last name'
            }),
            'type': forms.Select(attrs={
                'class': 'input'
            }),
            'category': forms.Select(attrs={
                'class': 'input'
            }),
            'level': forms.Select(attrs={
                'class': 'input'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number for feedback',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email for feedback',
            }),

            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Additional information...',
                'rows': 4
            }),
            'resume_file': forms.FileInput(attrs={
                'class': 'input',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
            'uploaded_at': forms.DateTimeInput(attrs={
                'class': 'input',
                'type': 'datetime-local',
                'readonly': 'readonly'
            }),
        }
class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter your first and last name'
            }),
            'type': forms.Select(attrs={
                'class': 'input'
            }),
            'level': forms.Select(attrs={
                'class': 'input'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number for feedback',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email for feedback',
            }),

            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Additional information...',
                'rows': 4
            }),
            'resume_file': forms.FileInput(attrs={
                'class': 'input',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
            'uploaded_at': forms.DateTimeInput(attrs={
                'class': 'input',
                'type': 'datetime-local',
                'readonly': 'readonly'
            }),
        }
class YoungVacancyForm(forms.ModelForm):
    class Meta:
        model = YoungVacancy
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter your first and last name'
            }),
            'years': forms.NumberInput(attrs={
                'class': 'input',
                'placeholder': 'How old are you?',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number for feedback',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email for feedback',
            }),

            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Additional information...',
                'rows': 4
            }),
            'resume_file': forms.FileInput(attrs={
                'class': 'input',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
            'uploaded_at': forms.DateTimeInput(attrs={
                'class': 'input',
                'type': 'datetime-local',
                'readonly': 'readonly'
            }),
        }
class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter your first and last name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number for feedback',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email for feedback',
            }),
            'money': forms.NumberInput(attrs={
                'class': 'input',
                'placeholder': 'Approximately how much are you willing to invest ($)?',
            }),

            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Additional information...',
                'rows': 4
            }),
            'document': forms.FileInput(attrs={
                'class': 'input',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
        }
class cooperationForm(forms.ModelForm):
    class Meta:
        model = cooperation
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter your first and last name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number for feedback',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email for feedback',
            }),

            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Additional information...',
                'rows': 4
            }),
            'document': forms.FileInput(attrs={
                'class': 'input',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
        }
class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter your first and last name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number for feedback',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email for feedback',
            }),

            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Additional information...',
                'rows': 4
            }),
            'document': forms.FileInput(attrs={
                'class': 'input',
                'accept': '.pdf,.doc,.docx,.txt'
            }),
        }
