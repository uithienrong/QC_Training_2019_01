import datetime
import random

names=['Le Huu Tai','Dinh Thi Luu Uy','Pham Dinh Anh Quan','Dinh Thi Luu Xuyen','Pham Dinh Di Bang','Phan Ngoc Thach','Nguyen Thi Kieu Lam', 'Phan Thanh Thao','Truong Thi Thu Huong','Ung Thi Bich Nga']
gender=['male', 'female']
education=['QNU','Da Nang University','NEU','Tp. HCM University','Da Lat University','Sai Gon University','HUTECH','VHU','HUST']
street=['An Duong Vuong','Vo Thi Yen','Nguyen Tat Thanh','Mai Xuan Thuong','Nguyen Hue','Nguyen Thai Hoc']
district=['An Nhon','Qui Nhon','Tuy Phuoc','Tay Son','An Lao','Phu Cat']
skill=['Java','Python','PHP','C#','C++','MySql']
hobbies=['music','badminton','shopping','soccer','football','swimming','climbing','read books']	

class Person:
	def __init__( self,name, gender, education, birthday, address, phone, skill, hobbies):
		self.name=name
		self.gender=gender
		self.education=education
		self.birthday=birthday
		self.address=address
		self.phone=phone
		self.skill=skill
		self.hobbies=hobbies

def getname():
    names1= []
    names1=random.sample(names,10)
    return names1

def getgender():
    genders= []
    genders.append(random.choice(gender))
    return genders

def geteducation():
    educations= []
    educations.append(random.choice(education))
    return educations

def getphone():
    phones=[0]
    for x in range(9):
    	phones.append(str(random.randint(0,9)))
    return phones

def getskill():
	getskills=[]
	skills=random.sample(skill, random.randint(2,3)) 
	for i in skills:
		Empirical=i+'({} year)'.format(random.randint(1,3))
		getskills.append(Empirical)
	return getskills

def gethobbies():
	hobbiesget=[]
	hb=random.sample(hobbies, random.randint(1,3))
	for i in hb:
		hobbiesget.append(i)
	return hobbiesget

def getbirthday():
    year=[]
    month=[]
    day=[]
    birthday=[]
    year=random.randint(1995,2000)
    month=random.randint(1,12)
    if month in [1,3,5,7,8,10,12]:
    	day=random.randint(1,31)
    elif month in [4,6,9,11]:
    	day=random.randint(1,30)
    else:
    	day=random.randint(1,28)
    birthday.append(day)
    birthday.append('/')
    birthday.append(month)
    birthday.append('/')
    birthday.append(year)
    return birthday

def getAddress():
	getaddress=[]
	randomaddress=str(random.randint(1,999)) +' '+ random.choice(street) +', '+ random.choice(district)+ ', Binh Dinh'
	getaddress.append(randomaddress)
	return getaddress

def printPerson():
	username=getname()

	for i in username:
		person=Person(i,getgender(),geteducation(),getbirthday(),getAddress(),getphone(), getskill(), gethobbies())

		chuoiphone=''
		for j in person.phone:
			chuoiphone=chuoiphone+str(j)
		f=open('CV-{}.txt'.format(i.upper()), 'w')
		f.write('Name: {}\n'.format(''.join(person.name)))
		f.write('gender: {}\n'.format(','.join(person.gender)))
		f.write('education: {}\n'.format(','.join(person.education)))
		f.write('address: {}\n'.format(','.join(person.address)))
		f.write('phone: {}\n'.format(''.join(chuoiphone)))
		f.write('skill: {}\n'.format(','.join(person.skill)))
		f.write('hobbies: {}\n'.format(','.join(person.hobbies)))
printPerson()

