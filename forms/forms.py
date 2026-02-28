from django import forms
from .models import DisabilityVacancy

class DisabilityVacancyForm(forms.ModelForm):
    class Meta:
        model = DisabilityVacancy
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Введите имя и фамилию'
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
            'text': forms.Textarea(attrs={
                'class': 'input',
                'placeholder': 'Дополнительная информация...',
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