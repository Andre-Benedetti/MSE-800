
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from uploader.bmi import calculate_bmi_info

def home_page(request):
    return render(request, 'home.html')

def bmi_page(request):
    result = None
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        result = calculate_bmi_info(weight, height)
    return render(request, 'bmi.html', {'result': result}) # Points to bmi.html

def upload_page(request):
    image_url = None
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

    return render(request, 'upload.html', {'image_url': image_url})
