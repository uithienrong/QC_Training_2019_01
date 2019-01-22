 # -*- coding: utf-8 -*-
import datetime
import random


name=['NGO THE HUAN','LAM DUAN NHI','LY DONG HAI','BAC CAN NGON','CHAU SUNG QUAN','LA TAN','BUI CHAU HUYEN','DIEM LINH CO','HOANG MY ANH', 'KIM THAI NGHIEN','TRINH TU NGHIEN','SUHO','TU CHAU HIEN','JACKSON']
gender=['male', 'female']
education=['UIT','VHU','QNU','NEU','TDTU','HNUE','RMIT','UL','QSY','HUTECH']
street=['Tran Phu','Nguyen Tat Thanh','An Duong Vuong','Nguyen Thai Hoc','Tran Van On']
district=['An Nhon','Qui Nhon','Tuy Phuoc','Tay Son','An Lao','Phu Cat']
skill=['C','Java','Ruby','Swift','Python','C#','PHP','C++']
hobbies=['music','badminton','chess','dance','football','volleyball','tenis']


class Person:
	def __init__(self, name, gender, education, birthday, address, phone, skill, hobbies):
		self.name=name
		self.gender=gender
		self.education=education
		self.birthday=birthday
		self.address=address
		self.phone=phone
		self.skill=skill
		self.hobbies=hobbies


def getGender():
	return random.choice(gender)


def getEducation():
	return random.choice(education)


def getDate():
	t=datetime.date.today()
	year=random.randint(t.year-25, t.year-20) 
	month=random.randint(1,12)
	if month in [1,3,5,7,8,10,12]:
		dates=random.randint(1,31)
	elif month in [4,6,9,11]:
		dates=random.randint(1,30)
	else:
		dates=random.randint(1,28) 

	return str(dates)+'-'+str(month)+'-'+str(year)


def getAddress():
	getaddress=[]
	randomaddress=str(random.randint(1,999)) +' '+ random.choice(street) +', '+ random.choice(district)+ ', Binh Dinh.'
	getaddress.append(randomaddress)
	return getaddress


def getPhone():
	getphone=[]
	randomphone='0'+str(random.randint(100000000,999999999))
	getphone.append(randomphone)
	return getphone


def getSkill():
	getskill=[]
	randomskill=random.sample(skill, random.randint(3,3))
	for i in randomskill:
		Experience=i+'('+str(random.randint(1,3))+' year)'
		getskill.append(Experience)
	return getskill


def getHobbies():
	gethobbies=[]
	hobb=random.sample(hobbies, random.randint(2,2))
	for i in hobb:
		gethobbies.append(i)
	return gethobbies

def main():
	username=random.sample(name,10)

	for i in username:
		person=Person(i,getGender(),getEducation(),getDate(),getAddress(),getPhone(), getSkill(), getHobbies())

		saddress=''
		for j in person.address:
			saddress=saddress+j

		sphone=''
		for j in person.phone:
			sphone=sphone+j

		sskill=''
		for j in person.skill:
			sskill=sskill+j+', '

		shobbies=''
		for j in person.hobbies:
			shobbies=shobbies+j+', '

		file=open('CV-'+i+'.txt', 'w')
		file.write(i+'\n')
		file.write('gender: '+getGender()+'\n')
		file.write('education: '+getEducation()+'\n')
		file.write('birthday: '+str(getDate())+'\n')
		file.write('address: '+saddress+'\n')
		file.write('phone: '+sphone+'\n')
		file.write('skill: '+sskill+'\n')
		file.write('hobbies: '+shobbies+'\n')
		file.close();

main()
