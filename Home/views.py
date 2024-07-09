from django.shortcuts import render, HttpResponse
from Home.models import Blog, Contact
import math
# Create your views here.
def home(request):
	return render(request,'index.html')

def blog(request):
	no_of_post = 3
	# print(request.GET)
	page = request.GET.get('page')
	if page is None:
		page=1
	else:
		page = int(page)
	# print(page)	
	'''
	1 : 0 - 3
	2 : 3 - 6
	3 : 6 - 9
	
	1 : 0 to 0 + no_of_post
	2 : no_of_post to no_of_post+no_of_post
	3 : no_of_post+no_of_post to no_of_post + no_of_post + no_of_post

	formula
	(page_no-1) to page_no*no_of_post
	'''
	blogs = Blog.objects.all()
	length = len(blogs)
	blogs=blogs[(page-1)*no_of_post:page*no_of_post]
	if page>1:
		prev = page -1
	else : 
		prev = None

	if page < math.ceil(length/no_of_post):    #no. of pages 
		# '''
		# 3.67 : 4
		# 5.66 : 6
		# '''
		nxt = page + 1		
	else : 		
		nxt = None
	context = {'blogs' : blogs , 'prev': prev , 'nxt' : nxt}
	# print(prev,nxt)
	return render(request,'bloghome.html',context)

def blogpost(request , slug):
	blog = Blog.objects.filter(slug=slug).first()
	context = {'blog' : blog}
	# return HttpResponse(f"you r viewing {slug}")
	return render (request, 'blogpost.html',context)

# some random address in url

def contact(request):
	if request.method=='POST':
		# is_private = request.POST['is_private']
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		phone = request.POST.get('phone')
		Email = request.POST.get('Email')
		Password = request.POST.get('Password')
		Address = request.POST.get('Address')
		Problem = request.POST.get('Problem')
		# print(firstname,lastname,phone,Email,Password,Address,Problem)
		ins = Contact(firstname=firstname,lastname=lastname,phone=phone,Email=Email,Password=Password,Address=Address,Problem=Problem)
		ins.save()
		# print("data has been written in database")
	return render(request,'contact.html')

def search(request):
	return render(request,'search.html')