from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import UploadCallVolumesForm
from .models import CallLogs
from .cleanup import read_raw_data, call_volumes_cleanup
 
# Create your views here.
def calllogs(request):
    # return HttpResponse('I work!')
    logs = CallLogs.objects.all().order_by('-call_time')
    page = request.GET.get('page',1)

    paginator = Paginator(logs,500) # 100 call logs per page
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    # page_obj = paginator.get_page(page_number)
    return render(request,'callcenter/dashboard.html', {'page_objs': page_obj})

# def form_test(request):
#     form = FormTest()
#     if request.method == "POST":
#         form = FormTest(request.POST)
#         if form.is_valid:
#             form.save()
        
#     context = {'form': form}
#     return render(request,'callcenter/form_test.html', context)

def call_volumes(request):
    form = UploadCallVolumesForm()
    if request.method == "POST" and request.FILES['Call Volumes']:
        form = UploadCallVolumesForm(request.FILES)
        if form.is_valid:
            file_obj = request.FILES['Call Volumes']
            str_text = ''
            x = []
            for line in file_obj:
                str_text = str_text + line.decode(encoding = 'UTF-8',errors = 'strict')
            #print(str_text)
            #str_text = str_text[25:]
            read_raw_data(str_text)
            #read_raw_data(file_obj)
            #call_volumes_cleanup('callcenter/RawData.csv')
    context = {}
    return render(request, 'callcenter/form_test.html', context)