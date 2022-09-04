from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import FileModel
from django.core.files.base import ContentFile
import base64
# Create your views here.
def index(request):
    return render(template_name="index.html", request=request)
    
def upload_file(request):
    print("TT")
    file = request.FILES.get("file")
    fss = FileSystemStorage()
    filename = fss.save(file.name, file)
    url = fss.url(filename)
    print(file.name)
    data = ContentFile(base64.b64decode(file), name=file.name) 
    FileModel.objects.create(doc=data)
    print(data)
    return JsonResponse({"link": data})

def download_file(request):
    file=open('media/test.csv','rb')
    response =HttpResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="example.csv"'  
    return response