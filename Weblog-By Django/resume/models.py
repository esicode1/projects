from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from account.models import User
from django.core.exceptions import ValidationError
import os

def validate_jpg_png_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.jpg','.png']
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension. Just .jpg or .png')

def validate_zip_rar_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.zip','.rar']
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension. Just .zip or .rar')

class UserProfile(models.Model):
    user =          models.OneToOneField(User, on_delete=models.CASCADE)
    avatar =        models.FileField(upload_to='images/user_avatar/',null=False,blank=False,validators=[validate_jpg_png_file])
    description =   models.CharField(max_length=512,null=True, blank=True)

    def __str__(self):
        # return self.user.first_name + ' ' + self.user.last_name
        return self.user.username
        
class Category(models.Model):
    title =         models.CharField(max_length=128,null=False, blank=False)
    slug =          models.SlugField(max_length=128,unique=True)
    
    def __str__(self):
        return self.title
        
