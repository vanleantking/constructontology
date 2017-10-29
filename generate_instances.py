from owlready2 import *
onto = get_ontology("http://test.org/newemr.owl")

#Generate instance Age
def generateAge(onto, medicalRecord, info):
	with onto:
		age = onto.Age(info.attrib.get('text'))
		age.hasAge = [info.attrib.get('text')]
		age.hasStartPosition = [info.attrib.get('start')]
		age.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_record_at_age.append(age)
	onto.save(file="newemr.owl", format = "rdfxml")


#Generate instance Email
def generateEmail(onto, medicalRecord, info):
	with onto:
		email = onto.Email(info.attrib.get('text'))
		email.emailAddress = [info.attrib.get('text')]
		email.hasStartPosition = [info.attrib.get('start')]
		email.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(email)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Phone
def generatePhone(onto, medicalRecord, info):
	with onto:
		phone = onto.Phone(info.attrib.get('text'))
		phone.phoneNumber = [info.attrib.get('text')]
		phone.hasStartPosition = [info.attrib.get('start')]
		phone.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(phone)
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance URL
def generateURL(onto, medicalRecord, info):
	with onto:
		url = onto.URL(info.attrib.get('text'))
		url.urlAddress = [info.attrib.get('text')]
		url.hasStartPosition = [info.attrib.get('start')]
		url.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(url)
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Fax
def generateFax(onto, medicalRecord, info):
	with onto:
		fax = onto.Fax(info.attrib.get('text'))
		fax.faxNumber = [info.attrib.get('text')]
		fax.hasStartPosition = [info.attrib.get('start')]
		fax.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(fax)
	onto.save(file="newemr.owl", format = "rdfxml")


#Generate instance Date
def generateDate(onto, medicalRecord, info):
	with onto:
		date = onto.Date(info.attrib.get('text'))
		date.hasDate = [info.attrib.get('text')]
		date.hasStartPosition = [info.attrib.get('start')]
		date.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_observation_date.append(date)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Device
def generateDevice(onto, medicalRecord, info):
	with onto:
		device = onto.Device(info.attrib.get('text'))
		device.deviceID = [info.attrib.get('text')]
		device.hasStartPosition = [info.attrib.get('start')]
		device.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.was_use_device.append(device)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Doctor
def generateDoctor(onto, medicalRecord, info):
	with onto:
		doctor = onto.Doctor(info.attrib.get('text'))
		doctor.hasName = [info.attrib.get('text')]
		doctor.hasStartPosition = [info.attrib.get('start')]
		doctor.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.doctor_dianose.append(doctor)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Hospital
def generateHospital(onto, medicalRecord, info):
	with onto:
		hospital = onto.Hospital(info.attrib.get('text'))
		hospital.hasName = [info.attrib.get('text')]
		hospital.hasStartPosition = [info.attrib.get('start')]
		hospital.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.record_from_hospital.append(hospital)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance BioID
def generateBioID(onto, medicalRecord, info):
	with onto:
		bioID = onto.BioID(info.attrib.get('text'))
		bioID.hasUniqueID = [info.attrib.get('text')]
		bioID.hasStartPosition = [info.attrib.get('start')]
		bioID.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_unique_ID.append(bioID)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance HealthPlan
def generateHealthPlan(onto, medicalRecord, info):
	with onto:
		healthplan = onto.HealthPlan(info.attrib.get('text'))
		healthplan.hasUniqueID = [info.attrib.get('text')]
		healthplan.hasStartPosition = [info.attrib.get('start')]
		healthplan.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_unique_ID.append(healthplan)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance IDNum
def generateIDNum(onto, medicalRecord, info):
	with onto:
		idNum = onto.IDNum(info.attrib.get('text'))
		idNum.hasUniqueID = [info.attrib.get('text')]
		idNum.hasStartPosition = [info.attrib.get('start')]
		idNum.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_unique_ID.append(idNum)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance City
def generateCity(onto, medicalRecord, info):
	with onto:
		city = onto.City(info.attrib.get('text'))
		city.hasLocation = [info.attrib.get('text')]
		city.hasStartPosition = [info.attrib.get('start')]
		city.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(city)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Country
def generateCountry(onto, medicalRecord, info):
	with onto:
		country = onto.Country(info.attrib.get('text'))
		country.hasLocation = [info.attrib.get('text')]
		country.hasStartPosition = [info.attrib.get('start')]
		country.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(country)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance LocationOther
def generateLocationOther(onto, medicalRecord, info):
	with onto:
		locationOther = onto.LocationOther(info.attrib.get('text'))
		locationOther.hasLocation = [info.attrib.get('text')]
		locationOther.hasStartPosition = [info.attrib.get('start')]
		locationOther.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(locationOther)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Organization
def generateOrganization(onto, medicalRecord, info):
	with onto:
		organization = onto.Organization(info.attrib.get('text'))
		organization.hasLocation = [info.attrib.get('text')]
		organization.hasStartPosition = [info.attrib.get('start')]
		organization.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(organization)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance State
def generateState(onto, medicalRecord, info):
	with onto:
		state = onto.State(info.attrib.get('text'))
		state.hasLocation = [info.attrib.get('text')]
		state.hasStartPosition = [info.attrib.get('start')]
		state.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(state)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Street
def generateStreet(onto, medicalRecord, info):
	with onto:
		street = onto.Street(info.attrib.get('text'))
		street.hasLocation = [info.attrib.get('text')]
		street.hasStartPosition = [info.attrib.get('start')]
		street.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(street)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Zip
def generateZip(onto, medicalRecord, info):
	with onto:
		zipNumber = onto.Zip(info.attrib.get('text'))
		zipNumber.hasLocation = [info.attrib.get('text')]
		zipNumber.hasStartPosition = [info.attrib.get('start')]
		zipNumber.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_adddress.append(zipNumber)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance MedicalRecord
def generateMedicalRecord(onto, medicalRecord, info):
	with onto:
		medicalRecord.hasMedicalRecordID = [info.attrib.get('text')]
		medicalRecord.hasStartPosition = [info.attrib.get('start')]
		medicalRecord.hasEndPosition = [info.attrib.get('end')]
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Patient
def generatePatient(onto, medicalRecord, info):
	with onto:
		patient = onto.Patient(info.attrib.get('text'))
		patient.hasName = [info.attrib.get('text')]
		patient.hasStartPosition = [info.attrib.get('start')]
		patient.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.was_recorded_for.append(patient)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Username
def generateUsername(onto, medicalRecord, info):
	with onto:
		username = onto.Username(info.attrib.get('text'))
		username.hasName = [info.attrib.get('text')]
		username.hasStartPosition = [info.attrib.get('start')]
		username.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.was_recorded_for.append(username)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Profession
def generateProfession(onto, medicalRecord, info):
	with onto:
		profession = onto.Profession(info.attrib.get('text'))
		profession.jobName = [info.attrib.get('text')]
		profession.hasStartPosition = [info.attrib.get('start')]
		profession.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.job_position.append(profession)
		
	onto.save(file="newemr.owl", format = "rdfxml")