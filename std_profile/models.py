from django.db import models
from django.utils import timezone


    
#"first_name","last_name","date_of_birth","age","gender","state","city_street","postal_code","email","phone_number","secondary_rate","mother_lunguage","pyment_method","created_at","university_message",

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)
# Create your models here.
class Std_profile(models.Model):
    
    image=models.ImageField(upload_to='media',blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    date_of_birth=models.DateTimeField(auto_now=False)

    age=models.IntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    state=models.CharField(max_length=40)
    city_street= models.CharField(max_length=100)
    postal_code=models.IntegerField()
    email=models.EmailField(max_length=254)
    phone_number=models.IntegerField()
    secondary_rate=models.IntegerField()
    mother_lunguage=models.CharField(max_length=40)
    pyment_method=models.CharField(max_length=40)
    created_at = models.DateTimeField(default = timezone.now)
    university_message=models.TextField(max_length=1000)

def __str__(self):
    return self.first_name
