from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            ob =  Document.objects.latest('id').id
            ins = Document.objects.get(id =ob)
            gray(ins.document.url)
            ins.output = "output/output.jpg"
            ins.save()
            #input_path = upload_img.document
            #output_path = "/media/output/" + input_path
            return redirect('upload')
    else:
        form = DocumentForm()
        input_path = Document.objects.latest('id').id
        ins = Document.objects.get(id =input_path)
    return render(request, 'saize/model_form_upload.html', {
        'form': form,
        'obj':ins,
    })


def gray(url):
    path = str(settings.BASE_DIR) + url

    print(path)
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    output = str(settings.BASE_DIR) + "/media/output/output.jpg"
    cv2.imwrite(output, img_gray)
# Create your views here.
