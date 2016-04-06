from django.db import models
import json, re

class DPUser(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50,primary_key=True)
	password = models.CharField(max_length=50, default = 'happy')


	def __str__(self):
		name = "%s %s" % (self.first_name, self.last_name)
		return name

	def __unicode__(self):
		return self.first_name

	def getResponseData(self):
		response_data = {}
		response_data["success"] = True
		response_data["first_name"] = self.first_name
		response_data["last_name"] = self.last_name
		response_data["email"] = self.email
		return response_data

	# """
		# Optional methods
	# """

	def __hash__(self):
		return self.id

	def __cmp__(self, other):
		return self.id - other.id

	#class Meta:
		# ordering = ('first_name',)

class Preference(models.Model):
	preference = models.CharField(max_length=50)
	user = models.ForeignKey('DPUser',models.SET_NULL,
    blank=True,
    null=True,)
	


	def __str__(self):
		preference = "%s" % (self.preference)
		return preference

	def __unicode__(self):
		return self.preference

	def getResponseData(self):
		response_data = {}
		response_data["id"] = self.id
		response_data["preference"] = self.preference
		return response_data

	# """
		# Optional methods
	# """

	def __hash__(self):
		return self.id

	def __cmp__(self, other):
		return self.id - other.id

class Favorite(models.Model):
	placeid = models.CharField(max_length=50)
	user = models.ForeignKey('DPUser',models.SET_NULL,  blank=True, null=True,)
	

	def getResponseData(self):
		response_data = {}
		response_data["place_id"] = self.placeid
		response_data["user"] = self.user.getResponseData();
		return response_data

class Visited(models.Model):
	placeid = models.CharField(max_length=50)
	visit_date = models.DateField(auto_now=True, auto_now_add=False)
	user = models.ForeignKey('DPUser',models.SET_NULL,  blank=True, null=True,)

	def getResponseData(self):
		response_data = {}
		response_data["place_id"] = self.placeid
		response_data["user"] = self.user.getResponseData();
		response_data["visit_date"] = str(self.visit_date);
		return response_data



