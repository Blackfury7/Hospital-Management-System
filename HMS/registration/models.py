from django.db import models



class patients(models.Model):

	name = models.CharField(max_length = 200)
	dob = models.CharField(max_length = 50)

	username = models.CharField(max_length = 200)
	height = models.CharField(max_length = 10)
	weight = models.CharField(max_length = 10)

	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200, default = "1234")
	status = models.CharField(max_length = 20, default = 'Active')
	phone_no = models.CharField(max_length = 20, default =" ")
	gender = models.CharField(max_length = 20, default =" ")
	photo = models.CharField(max_length = 1000, blank=True)
	blood = models.CharField(max_length = 5, blank=True)
	address = models.CharField(max_length = 200, blank=True)
	




class doctors(models.Model):

	name = models.CharField(max_length = 200)

	username = models.CharField(max_length = 200)
	dob = models.CharField(max_length = 50)
	# experience = models.CharField(max_length = 20)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200, default = "1234")
	status = models.CharField(max_length = 20, default = 'Active')
	phone_no = models.CharField(max_length = 20, default =" ")
	gender = models.CharField(max_length = 20, default =" ")

	photo = models.CharField(max_length = 1000, blank=True)
	department = models.CharField(max_length = 200,default="doctor")