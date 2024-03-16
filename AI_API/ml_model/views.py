from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image



#def index(request):
#    if request.method == "POST":
#        form = ImageForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            # Отримання оновленого списку фотографій після збереження форми
#            img = Image.objects.all()
#            return render(request, "index.html", {"img": img, "form": form})
#    else:
#        form = ImageForm()
#
#    # Отримання списку всіх фотографій для відображення на сторінці
#    img = Image.objects.all()
#    return render(request, "index.html", {"img": img, "form": form})


def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            latest_image = Image.objects.latest('id')
            return render(request, "index.html", {"form": form, "latest_image": latest_image, 'image_class_choices': Image.class_choices})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "index.html", {"img": img, "form": form,'image_class_choices': Image.class_choices})

def results_page(request):
    results = Image.objects.all().order_by('-id')
    return render(request, 'results.html', {'img': results})