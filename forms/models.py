from django.db import models

# Create your models here.
class DisabilityVacancy(models.Model):
    
    
    EMPLOYMENT_TYPES = [
    ('full_time', 'Full time'),
    ('part_time', 'Part time'),
    ('remote', 'Remote'),
    ('internship', 'Internship'),
    ('flexible', 'Flexible schedule'),
]

    DISABILITY_CATEGORIES = [
    ('visual', 'Visual impairment'),
    ('hearing', 'Hearing impairment'),
    ('musculoskeletal', 'Musculoskeletal disorders'),
    ('mental', 'Mental health conditions'),
    ('speech', 'Speech impairment'),
    ('other', 'Other disabilities'),
]
    
    # Образование
    EDUCATION_LEVELS = [
    ('none', 'No education'),
    ('secondary', 'Secondary education'),
    ('vocational', 'Vocational education'),
    ('higher', 'Higher education'),
    ('academic', 'Academic degree'),
]
    name_and_surname = models.CharField(max_length=200)
    type = models.CharField(max_length=250, choices=EMPLOYMENT_TYPES)
    category = models.CharField(max_length=250,choices=DISABILITY_CATEGORIES)
    level = models.CharField(max_length=250,choices=EDUCATION_LEVELS)
    text = models.TextField('Additionally, I would like to specify:',null=True,blank=True)

    resume_file = models.FileField(
    upload_to='resumes/', 
    verbose_name="Резюме",
    blank=True, null=True
)
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    
    def __str__(self):
        return self.name_and_surname