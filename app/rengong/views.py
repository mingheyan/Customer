from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    # data = request.POST.get("spoken")
    # print(data)
    return render(request, '客服/new_service.html')
def data_info(request):
    if request.content_type == 'application/json':
        import json
        json_data = json.loads(request.body.decode('utf-8'))
        print(json_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     data = request.POST.get('spoken','jjjjj')
    #     print(data)
        return HttpResponse('ji')


