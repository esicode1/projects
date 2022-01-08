from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

from resume.models import (
	UserProfile,
	Category,
	validate_zip_rar_file,
	validate_jpg_png_file,
	)

class Project(models.Model):
    title = models.CharField(max_length=128,null=False, blank=False)
    content = RichTextField()
    slug = models.SlugField(max_length=100, unique=True, null=False, blank=False)
    file = models.FileField(upload_to='projects/',null=False, blank=False,validators=[validate_zip_rar_file])
    cover = models.FileField(upload_to='images/project_cover/',null=False, blank=False,validators=[validate_jpg_png_file])
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']