from django.shortcuts import render
import json
# Create your views here.
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method == 'POST':
		recieved_json_data = json.loads(request.body.decode("utf-8"))
		print('it was post request:'+ str(received_json_data))
		return StreamingHttpResponse('it was post request: '+str(received_json_data))
	return StreamingHttpResponse('it was get request')