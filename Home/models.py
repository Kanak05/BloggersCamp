from django.db import models

# Create your models here.
class Blog(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	slug = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30) 
    phone = models.CharField(max_length=10) 
    Email = models.EmailField() 
    Password = models.CharField(max_length=10) 
    Address = models.CharField(max_length=30) 
    Problem = models.TextField() 
    def __str__(self):
        return self.firstname + " " + self.lastname	