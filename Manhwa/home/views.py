from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({'file_location': settings.AWS_S3_CUSTOM_DOMAIN}, request))