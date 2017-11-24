from owlready2 import *
onto = get_ontology("http://test.org/newemr.owl")

#Generate instance Age
def generateAge(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		age = onto.Age(nameInstance)
		age.hasAge = [info.attrib.get('text')]
		age.hasStartPosition = [info.attrib.get('start')]
		age.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_record_at_age.append(age)
	onto.save(file="newemr.owl", format = "rdfxml")


#Generate instance Email
def generateEmail(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		email = onto.Email(nameInstance)
		email.emailAddress = [info.attrib.get('text')]
		email.hasStartPosition = [info.attrib.get('start')]
		email.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(email)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Phone
def generatePhone(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		phone = onto.Phone(nameInstance)
		phone.phoneNumber = [info.attrib.get('text')]
		phone.hasStartPosition = [info.attrib.get('start')]
		phone.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(phone)
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance URL
def generateURL(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		url = onto.URL(nameInstance)
		url.urlAddress = [info.attrib.get('text')]
		url.hasStartPosition = [info.attrib.get('start')]
		url.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(url)
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Fax
def generateFax(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		fax = onto.Fax(nameInstance)
		fax.faxNumber = [info.attrib.get('text')]
		fax.hasStartPosition = [info.attrib.get('start')]
		fax.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_contact.append(fax)
	onto.save(file="newemr.owl", format = "rdfxml")


#Generate instance Date
def generateDate(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		date = onto.Date(nameInstance)
		date.hasDate = [info.attrib.get('text')]
		date.hasStartPosition = [info.attrib.get('start')]
		date.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_observation_date.append(date)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Device
def generateDevice(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		device = onto.Device(nameInstance)
		device.deviceID = [info.attrib.get('text')]
		device.hasStartPosition = [info.attrib.get('start')]
		device.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.was_use_device.append(device)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Doctor
def generateDoctor(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		doctor = onto.Doctor(nameInstance)
		doctor.hasName = [info.attrib.get('text')]
		doctor.hasStartPosition = [info.attrib.get('start')]
		doctor.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.doctor_dianose.append(doctor)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Hospital
def generateHospital(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		hospital = onto.Hospital(nameInstance)
		hospital.hasName = [info.attrib.get('text')]
		hospital.hasStartPosition = [info.attrib.get('start')]
		hospital.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.record_from_hospital.append(hospital)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance BioID
def generateBioID(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		bioID = onto.BioID(nameInstance)
		bioID.hasUniqueID = [info.attrib.get('text')]
		bioID.hasStartPosition = [info.attrib.get('start')]
		bioID.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_unique_BioID.append(bioID)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance HealthPlan
def generateHealthPlan(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		healthplan = onto.HealthPlan(nameInstance)
		healthplan.hasUniqueID = [info.attrib.get('text')]
		healthplan.hasStartPosition = [info.attrib.get('start')]
		healthplan.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_healthPlan.append(healthplan)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance IDNum
def generateIDNum(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		idNum = onto.IDNum(nameInstance)
		idNum.hasUniqueID = [info.attrib.get('text')]
		idNum.hasStartPosition = [info.attrib.get('start')]
		idNum.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_unique_IDNum.append(idNum)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance City
def generateCity(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		city = onto.City(nameInstance)
		city.hasLocation = [info.attrib.get('text')]
		city.hasStartPosition = [info.attrib.get('start')]
		city.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_city.append(city)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Country
def generateCountry(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		country = onto.Country(nameInstance)
		country.hasLocation = [info.attrib.get('text')]
		country.hasStartPosition = [info.attrib.get('start')]
		country.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_country.append(country)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance LocationOther
def generateLocationOther(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		locationOther = onto.LocationOther(nameInstance)
		locationOther.hasLocation = [info.attrib.get('text')]
		locationOther.hasStartPosition = [info.attrib.get('start')]
		locationOther.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_locationother.append(locationOther)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Organization
def generateOrganization(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		organization = onto.Organization(nameInstance)
		organization.hasLocation = [info.attrib.get('text')]
		organization.hasStartPosition = [info.attrib.get('start')]
		organization.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_organization.append(organization)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance State
def generateState(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		state = onto.State(nameInstance)
		state.hasLocation = [info.attrib.get('text')]
		state.hasStartPosition = [info.attrib.get('start')]
		state.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_state.append(state)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Street
def generateStreet(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		street = onto.Street(nameInstance)
		street.hasLocation = [info.attrib.get('text')]
		street.hasStartPosition = [info.attrib.get('start')]
		street.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_street.append(street)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Zip
def generateZip(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		zipNumber = onto.Zip(nameInstance)
		zipNumber.hasLocation = [info.attrib.get('text')]
		zipNumber.hasStartPosition = [info.attrib.get('start')]
		zipNumber.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_zip.append(zipNumber)
		
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
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		patientRecord = medicalRecord.recorded_on_patient_record[0]
		patient = onto.Patient(nameInstance)
		patient.hasName = [info.attrib.get('text')]
		patient.hasStartPosition = [info.attrib.get('start')]
		patient.hasEndPosition = [info.attrib.get('end')]
		patientRecord.have_collect_patients.append(patient)
		medicalRecord.have_collect_patients.append(patient)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Username
def generateUsername(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		username = onto.Username(nameInstance)
		username.hasName = [info.attrib.get('text')]
		username.hasStartPosition = [info.attrib.get('start')]
		username.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.has_username.append(username)
		
	onto.save(file="newemr.owl", format = "rdfxml")

#Generate instance Profession
def generateProfession(onto, medicalRecord, info):
	nameInstance = "-".join([info.attrib.get('text'), medicalRecord.name, info.attrib.get('start')])
	with onto:
		profession = onto.Profession(nameInstance)
		profession.jobName = [info.attrib.get('text')]
		profession.hasStartPosition = [info.attrib.get('start')]
		profession.hasEndPosition = [info.attrib.get('end')]
		medicalRecord.job_position.append(profession)
		
	onto.save(file="newemr.owl", format = "rdfxml")