import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import DPUser


@csrf_exempt
def userRequest(request, user_email=None):
	 if request.method == "POST":
		return createUser(request)
	 else:
		return getUser(request, user_email)

@csrf_exempt
def createUser(request):
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	email = request.POST.get('email','')
	password = request.POST.get('password','')
	user = None
	existing_users = DPUser.objects.filter(email=email)

	if len(existing_users) > 0:
		# User Exists!
		user = existing_users[0]
		errorMessage = "Error! User with this email already exists."

		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if user is None:
		user = DPUser()

	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.password = password

	user.save()

	response_data = user.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getUser(request, user_email):
	response_data = {}
	
	if user_email :
		users = DPUser.objects.filter(email=user_email)	

		if len(users)>0:
			user = users[0]
			response_data = user.getResponseData()
		else:
			errorMessage = "Error! This user doesn't exist."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getActualUser(user_email):
	if user_email :
		users = DPUser.objects.filter(email=user_email)
	

		if len(users)>0:
			user = users[0]
			response_data = user.getResponseData()
		else:
			errorMessage = "Error! This user doesn't exist."
			response_data = {'success': False, "error":errorMessage}

	return user

