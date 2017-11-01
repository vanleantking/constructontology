import os
import sys
import xml.etree.ElementTree as ET
from owlready2 import *
import types
import generate_instances



BASE_DIR_DATA = '/media/vanle/Studying/python/word2vec/glove/data'

def construct_ontology():
    onto = get_ontology("http://test.org/newemr.owl")
    print(onto.data_properties())
    print(list(onto.classes()))
    with onto:
        #Define class object
        class Age(Thing):
            pass
        class Patient(Thing):
            pass
        class Doctor(Thing):
            pass
        class Contact(Thing):
            pass
        class ID(Thing):
            pass
        class Location(Thing):
            pass
        class Device(Thing):
            pass
        class Profession(Thing):
            pass
        class Username(Thing):
            pass
        class Date(Thing):
            pass
        class MedicalRecord(Thing):
            pass

        class Phone(Contact):
            pass
        class Fax(Contact):
            pass
        class Email(Contact):
            pass
        class URL(Contact):
            pass

        class Hospital(Location):
            pass
        class City(Location):
            pass
        class State(Location):
            pass
        class Street(Location):
            pass
        class Zip(Location):
            pass
        class Organization(Location):
            pass
        class Country(Location):
            pass
        class LocationOther(Location):
            pass

        class BioID(ID):
            pass
        class HealthPlan(ID):
            pass
        class IDNum(ID):
            pass


        #define object property - relation
        class has_city(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [City]

        class has_street(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [Street]

        class has_state(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [State]

        class has_organization(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [Organization]

        class has_country(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [Country]

        class has_locationother(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [LocationOther]

        class has_zip(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [Zip]

        class has_age(ObjectProperty):
            domain =[Patient]
            range = [Age]

        class record_from_hospital(ObjectProperty):
            domain =[MedicalRecord]
            range = [Hospital]

        class doctor_dianose(ObjectProperty):
            domain =[MedicalRecord]
            range = [Doctor]

        class has_unique_IDNum(ObjectProperty):
            domain =[MedicalRecord]
            range = [IDNum]

        class has_unique_BioID(ObjectProperty):
            domain =[MedicalRecord]
            range = [BioID]

        class has_healthPlan(ObjectProperty):
            domain =[MedicalRecord]
            range = [HealthPlan]

        class has_contact(ObjectProperty):
            domain =[Patient, Doctor, MedicalRecord]
            range = [Phone, Fax, Email, URL]

        class has_record_at_age(ObjectProperty):
            domain =[MedicalRecord]
            range = [Age]

        class job_position(ObjectProperty):
            domain =[Patient, MedicalRecord]
            range = [Profession]

        class has_observation_date(ObjectProperty):
            domain =[MedicalRecord]
            range = [Date]

        class was_recorded_for(ObjectProperty):
            domain =[MedicalRecord]
            range = [Patient]

        class has_username(DataProperty):
            domain = [MedicalRecord]
            range = [Username]
            
        class was_recorded_at(ObjectProperty):
            domain =[Patient]
            range = [MedicalRecord]
            inverse_property = was_recorded_for

        class was_treated_at(ObjectProperty):
            domain =[Patient]
            range = [Hospital]

        class was_use_device(ObjectProperty):
            domain =[MedicalRecord]
            range = [Device]

        #define data property
        class deviceID(DataProperty):
            domain = [Device]
            range = [str]

        class emailAddress(DataProperty):
            domain = [Email]
            range = [str]

        class faxNumber(DataProperty):
            domain = [Fax]
            range = [str]

        class hasAge(DataProperty):
            domain = [Age]
            range = [str]

        class hasDate(DataProperty):
            domain = [Date]
            range = [str]

        class hasUniqueID(DataProperty):
            domain = [ID]
            range = [str]

        class hasMedicalRecordID(DataProperty):
            domain = [MedicalRecord]
            range = [str]

        class hasLocation(DataProperty):
            domain = [Location]
            range = [str]

        class hasName(DataProperty):
            domain = [Doctor, Hospital, Patient, Username]
            range = [str]

        class jobName(DataProperty):
            domain = [Profession]
            range = [str]

        class phoneNumber(DataProperty):
            domain = [Phone]
            range = [str]

        class urlAddress(DataProperty):
            domain = [URL]
            range = [str]

        class hasSerialize(DataProperty):
            domain = [MedicalRecord]
            range = [int]

        class hasRecordName(DataProperty):
            domain = [Patient]
            range = [int]

        #data properties save info to de-identifier
        class hasStartPosition(DataProperty):
            domain = [Age, Email, Fax, Phone, URL, Date, Device, Doctor, Hospital, BioID, HealthPlan, IDNum, City, Country, LocationOther,
            Organization, State, Street, Zip, MedicalRecord, Patient, Profession, Username]
            range = [str]
        class hasEndPosition(DataProperty):
            domain = [Age, Email, Fax, Phone, URL, Date, Device, Doctor, Hospital, BioID, HealthPlan, IDNum, City, Country, LocationOther,
            Organization, State, Street, Zip, MedicalRecord, Patient, Profession, Username]
            range = [str]
        class hasCloneInfo(DataProperty):
            domain = [Age, Email, Fax, Phone, URL, Date, Device, Doctor, Hospital, BioID, HealthPlan, IDNum, City, Country, LocationOther,
            Organization, State, Street, Zip, MedicalRecord, Patient, Profession, Username]
            range = [str]

    onto.save(file="newemr.owl", format = "rdfxml")
    for name in sorted(os.listdir(BASE_DIR_DATA)):
        path = os.path.join(BASE_DIR_DATA, name)
        if os.path.isdir(path):
            for fname in sorted(os.listdir(path)):
                fpath = os.path.join(path, fname)
                patientRecord = fname.split("-")[0]
                tree = ET.parse(fpath)
                root = tree.getroot()
                tags = root.find('TAGS')
                with onto:
                    patientRecords = None
                    for patient in onto.Patient.instances():
                        if patientRecord == patient.name:
                            patientRecords = patient

                    if patientRecords is None:
                        patientRecords = onto.Patient(patientRecord)
                        patientRecords.hasRecordName = [patientRecord]
                    medicalRecord = onto.MedicalRecord(fname)
                    patientRecords.was_recorded_at.append(medicalRecord)
                    medicalRecord.hasSerialize = [fname]
                for child in tags.getiterator():
                    get_ontology_type(onto, medicalRecord, child)
    

def get_ontology_type(onto, medicalRecord, info):
    switcher = {
        "AGE": "generateAge",
        "EMAIL": "generateEmail",
        "FAX": "generateFax",
        "PHONE": "generatePhone",
        "URL": "generateURL",
        "DATE": "generateDate",
        "DEVICE": "generateDevice",
        "DOCTOR": "generateDoctor",
        "HOSPITAL": "generateHospital",
        "BIOID": "generateBioID",
        "HEALTHPLAN": "generateHealthPlan",
        "IDNUM": "generateIDNum",
        "CITY": "generateCity",
        "COUNTRY": "generateCountry",
        "LOCATIONOTHER": "generateLocationOther",
        "ORGANIZATION": "generateOrganization",
        "STATE": "generateState",
        "STREET": "generateStreet",
        "ZIP": "generateZip",
        "MEDICALRECORD": "generateMedicalRecord",
        "PATIENT": "generatePatient",
        "PROFESSION": "generateProfession",
        "USERNAME": "generateUsername"
    }
    generateinstance = switcher.get(info.attrib.get('TYPE'),"Thing")

    if (generateinstance != "Thing"):
        return getattr(generate_instances, generateinstance)(onto, medicalRecord, info)
    else:
        pass


if __name__ == '__main__':
    construct_ontology()
    print("Construct Ontology EMR complete!!!")