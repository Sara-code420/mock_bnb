# mock_bnb
 A simple outlook using Django to replicate hotels/stays website

 Project Documentation 
  

main page url : http://127.0.0.1:8000/bnb/
admin page url : http://127.0.0.1:8000/admin/
Mockbnb is a link to home page 


start a project : with command - Django-admin startproject projectname {mockbnb} -

Test:  by running the project - python manage.py runserver - and test by copy paste that URL in web , also test with URL extension '/admin' 

setting.py : check if you have installed app in setting.py - 'django.contrib.admin' to set up superuser 

creating an app: with command - python manage.py startapp appname {bnb} - and bnb folder was created with migrations folder

urls.py: create a file in bnb {file name to be exaclty - urls.py} import path from django.urls and import views from the same directory with command -from django.urls import path
and from . import views -. Now code to add the created view in the list

	urlpatterns = [
		path('bnb/', views.index)
	]
	
orginal mockbnb directory urls.py: code to 'include' and add the created 'bnb.urls' to existing urlpatterns list 

	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', include('bnb.urls'))
	]
	

settings.py : add the app in settings.py in directory mockbnb as -'bnb'-

	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'bnb'
	]
	
understanding urls.py : bnb urls.py and mockbnb urls.py 

	extensions can be modified - code modified 

	bnb urls.py - 

		urlpatterns = [
				path('', views.index)
			]

	mockbnb urls.py - 

		from django.contrib import admin
		from django.urls import path, include

		urlpatterns = [
			path('admin/', admin.site.urls),
			path('bnb/', include('bnb.urls'))
		]

Creating models to create database table : code 

	from django.db import models

	# Create your models here.

	class Property(models.Model):
		PROPERTY_TYPES = [
			('house', 'House'),
			('apartment', 'Apartment'),
			('condo', 'Condo'),
			# Add more property types as needed
		]

		name = models.CharField(max_length=250)
		type = models.CharField(max_length=100, choices=PROPERTY_TYPES, default='house')
		location = models.CharField(max_length=250, default='')
		price = models.DecimalField(max_digits=9, decimal_places=2)
		coverImage = models.TextField()
		secondaryImage = models.TextField(default='')
		description = models.TextField()
		slug = models.SlugField(unique=True)
		numGuests = models.PositiveIntegerField()
		numBedrooms = models.PositiveIntegerField(default='0')
		numBathrooms = models.PositiveIntegerField(default='0')
			
Command : python3 manage.py makemigrations

Command : python3 manage.py migrate

passing variables in views.py:

	def index (request):

		propertylist = Property.objects.all()
		return render(request, 'bnb/index.html', {
			'show_properties': True,
			'properties': propertylist
		})

	def property_details(request, property_slug):
	 
		selectedProperty = Property.objects.get(slug=property_slug)

		return render (request, 'bnb/property-details.html',{
			'property' : selectedProperty
		})
		
adding slug property in urls for unique url 

	from django.urls import path
	from . import views 

	urlpatterns = [
		path('', views.index), #bnb 
		path('<slug:property_slug>', views.property_details),
	]
	
pass variables in homepage 

	{% for property in properties %}
				   <li class="property-item">
					  <article>
						 <div class="property-summary">
							<div class="property-image">
								<img src="{{ property.coverImage }}" alt="">
							</div>
							<div class="property-details">
								<h3>{{ property.name}}</h3>
								<p>{{ property.price }}</p>
							</div>
						 </div>
						 <div class="property-actions">
							<a href="{{ property.slug}}" class="btn">More Details</a>
						 </div>
					  </article>
				   </li>
				   {%endfor%}
				 
				 
adding variables in details page 

	<h1>{{ property.name }}</h1>
		</header>
		<main>
			<article>
				<img src="{{ property.coverImage }}" alt="picture not available">

				<section id="guests">
					<h2>Number of Guests</h2>
					<address>This property can have <span>{{property.numGuests}} guests.</span></address>
				</section>

				<section id="details">
					<h2>Property Details</h2>
					<ul>
						<li><strong>Type:</strong> {{ property.type }}</li>
						<li><strong>Location:</strong> {{ property.location }}</li>
						<li><strong>Price per Night:</strong> ${{ property.price }}</li>
						<li><strong>Number of Bedrooms:</strong> {{ property.numBedrooms }}</li>
						<li><strong>Number of Bathrooms:</strong> {{ property.numBathrooms }}</li>
					</ul>
				</section>

				<section>
					<h2>About Property</h2>
					<p>{{ property.description }}</p>
					<footer>
						<p>Need more details? Please <a href="">contact the admin</a> (but please don't spam us)</p>
					</footer>
				</section>
				
Utilizing django admin interface 

command : python3 manage.py createsuperuser

username : saranya
password : ******

adding models in admin.py 

	from django.contrib import admin
	from .models import Property
	# Register your models here.

	admin.site.register(Property)

Adding a property object 



python manage.py runserver 


