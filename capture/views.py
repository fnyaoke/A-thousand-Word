from django.http  import HttpResponse,Http404
from django.shortcuts import render
from .models import Image, Location, Category,ObjectDoesNotExist
from django import forms

from cloudinary.forms import cl_init_js_callbacks
from .forms import PhotoForm

# Create your views here.

def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'A Thousand Words'

    return render(request, 'index.html', {'title':title, 'image':images, 'location':locations})

def single(request,category_name,image_id):
    images = Image.get_image_by_id(image_id)
    title = 'Image'
    locations = Location.objects.all()
    image_category = Image.objects.filter(image_category__name = category_name)
    category = Category.get_category_id(id = image_category)
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"single.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})

def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'image': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You have not searched yet'
        return render(request, 'search.html',{"message": message})


def location_filter(request, image_location):
    locations = Location.objects.all()
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'image':images, 'locations':locations, 'location':location})


def category(request,search_term):
    categories = Image.get_image_by_cat(search_term)
    return render(request, 'category.html', {"categories": categories})

def upload(request):
    context = dict( backend_form = PhotoForm())
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
    if form.is_valid():
        form.save()
    return render(request, 'single.html', context)
