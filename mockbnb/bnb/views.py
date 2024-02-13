from django.shortcuts import render
from .models import Property

# Create your views here.
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