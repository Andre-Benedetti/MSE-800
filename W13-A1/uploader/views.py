from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Ensure get_llm_diet_suggestion is imported from your bmi.py
from uploader.bmi import calculate_bmi_info, get_llm_diet_suggestion

def home_page(request):
    return render(request, 'home.html')

def bmi_page(request):
    result = None
    diet_suggestion = None
    
    if request.method == 'POST':
        # Capturing the 3 factors from the form
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        # 1. Calculate BMI and Category
        result = calculate_bmi_info(weight, height)

        if result:
            # 2. Call the real GroqCloud LLM 
            diet_suggestion = get_llm_diet_suggestion(result, age, gender)

    return render(request, 'bmi.html', {
        'result': result, 
        'diet_suggestion': diet_suggestion
    })

def upload_page(request):
    image_url = None
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

    return render(request, 'upload.html', {'image_url': image_url})