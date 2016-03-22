import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Preference
import UserManager


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

	if len(existing) > 0:
		# User Exists!
		user = existing[0]
		errorMessage = "Error! Preference with this email already exists."

		return HttpResponse(json.dumps({'success': False, "error":errorMessage, 'existing':existing}), content_type="application/json")

	if newPreference is None:
		newPreference = Preference()

	#use usermanager method to get user we want
	user = UserManager.getActualUser(email)

	newPreference.preference = preference
	newPreference.user = user
	

	newPreference.save()

	response_data = newPreference.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getPreferences(request, user_email):
	response_data = {}
	
	#use usermanager method to get user we want
	user = UserManager.getActualUser(user_email)
	if user:
		prefs = Preference.objects.filter(user=user).values_list('preference')
		prefs = list(prefs)
		
		
		response_data["preferences"] = prefs

		if len(prefs)>0:
			#user = users[0]
			#response_data = user.getResponseData()
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			errorMessage = "Error! This user has no prefererences."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")


