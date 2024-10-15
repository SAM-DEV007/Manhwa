from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import Manhwa

import json

manhwa = Manhwa.objects.values_list('data', flat=True).get(pk=1)
manhwa = json.dumps(manhwa)

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({'file_location': settings.AWS_S3_CUSTOM_DOMAIN, 'json_data': manhwa}, request))