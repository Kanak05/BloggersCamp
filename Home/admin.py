from django.contrib import admin
from Home.models import Blog , Contact
# Register your models here.

class BloggersCampAdmin(admin.ModelAdmin):
	class Media: 
		css = {
			"All" : ("css/main.css")
		}

		js = ("js/blog.js")


admin.site.register(Blog, BloggersCampAdmin)
admin.site.register(Contact)