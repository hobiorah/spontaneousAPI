import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Visited
from ..models import Favorite
import UserManager
import random
from datetime import datetime
from datetime import date


@csrf_exempt
def visitRequest(request, user_email=None):
	 if request.method == "POST":
		return createVisit(request)
	 else:
		return getPreferences(request, user_email)

@csrf_exempt
def createVisit(request):
	place_id = request.POST.get('place_id','')
	email = request.POST.get('user','')
	newVisit = None
	existing = Visited.objects.filter(user=email).filter(placeid=place_id)

#check if the visit exists for the user 
	if len(existing) > 0:
		
		newVisit = existing[0]
		
		errorMessage = "Error! This place is already stored as a visited lcation."

		return HttpResponse(json.dumps({'success': False,"error":errorMessage, 'existed':True}), content_type="application/json")

#if the preference doesnt exist
	if newVisit is None:
		newVisit = Visited()

	#get the user we want to insert for
	user = UserManager.getActualUser(email)

	newVisit.placeid = place_id
	newVisit.user = user
	

	newVisit.save()

	response_data = newVisit.getResponseData()
	response_data["existed"] = False
	response_data["success"] = True


	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def visitable(request, user_email,place_id):
	response_data = {}
	response_data["success"] = False
	response_data["canVisit"] = False

	
	#use usermanager method to get user we want
	user = UserManager.getActualUser(user_email)
	if user:
		location = Visited.objects.filter(user=user).filter(placeid =place_id)

		if(location):
			response_data["success"] = True
			response_data["date"] = str(location[0].visit_date)
			since_last = (datetime.today().date() - location[0].visit_date).days
			response_data["since_last"] = since_last

			if(since_last >=30):
				response_data["canVisit"] = True


		else:#user hasnt visited this place before
			response_data["success"] = True
			response_data["canVisit"] = True


	else:
			errorMessage = "Error! This user has no visits."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def createFavorite(request):
	place_id = request.POST.get('place_id','')
	email = request.POST.get('user','')
	newFavorite = None
	existing = Favorite.objects.filter(user=email).filter(placeid=place_id)

#check if the Facvorite exists for the user 
	if len(existing) > 0:
		
		newFavorite = existing[0]
		
		errorMessage = "Error! This place is already favorited."

		return HttpResponse(json.dumps({'success': False,"error":errorMessage, 'existed':True}), content_type="application/json")

#if the preference doesnt exist
	if newFavorite is None:
		newFavorite = Favorite()

	#get the user we want to insert for
	user = UserManager.getActualUser(email)

	newFavorite.placeid = place_id
	newFavorite.user = user
	

	newFavorite.save()

	response_data = newFavorite.getResponseData()
	response_data["existed"] = False
	response_data["success"] = True


	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getFavorites(request, user_email):
	response_data = {}
	response_data["success"] = False
	
	#use usermanager method to get user we want
	user = UserManager.getActualUser(user_email)
	if user:
		favorites = Favorite.objects.filter(user=user).values_list('placeid')
		favorites = list(favorites)
		
		
		response_data["favorites"] = favorites
		

		if len(favorites)>0:
			response_data["success"] = True
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			errorMessage = "Error! This user has no favorites."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")
