import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Preference
import UserManager
import random


@csrf_exempt
def preferenceRequest(request, user_email=None):
	 if request.method == "POST":
		return createPreference(request)
	 else:
		return getPreferences(request, user_email)

@csrf_exempt
def createPreference(request):
	preference = request.POST.get('preference','')
	email = request.POST.get('user','')
	newPreference = None
	existing = Preference.objects.filter(user=email).filter(preference=preference)

#check if the preference exists for the user 
	if len(existing) > 0:
		# User Exists!
		newPreference = existing[0]
		errorMessage = "Error! Preference with this email already exists."

		return HttpResponse(json.dumps({'success': False, "error":errorMessage, 'existing':True}), content_type="application/json")

#if the preference doesnt exist
	if newPreference is None:
		newPreference = Preference()

	#get the user we want to insert for
	user = UserManager.getActualUser(email)

	newPreference.preference = preference
	newPreference.user = user
	

	newPreference.save()

	response_data = newPreference.getResponseData()
	response_data["existing"] = True
	response_data["first_name"] = user.first_name
	response_data["last_name"] = user.last_name
	response_data["email"] = user.email
	response_data["success"] = True


	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getPreferences(request, user_email):
	response_data = {}
	response_data["success"] = False
	
	#use usermanager method to get user we want
	user = UserManager.getActualUser(user_email)
	if user:
		prefs = Preference.objects.filter(user=user).values_list('preference')
		prefs = list(prefs)
		
		
		response_data["preferences"] = prefs
		

		if len(prefs)>0:
			response_data["success"] = True
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			errorMessage = "Error! This user has no prefererences."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def randomPreference(request, user_email):
	
	#use usermanager method to get user we want
	user = UserManager.getActualUser(user_email)
	if user:
		prefs = Preference.objects.filter(user=user)
		prefs = list(prefs)

	if(len(prefs)>0):
		randomPref = random.randrange(0, len(prefs), 1)

		preference = Preference()
		preference = prefs[randomPref]
		response_data = preference.getResponseData()
		response_data["success"] = True
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		response_data = {}
		errorMessage = "Error! This user has no prefererences."
		response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")






