import datetime
import random
class CV:
	def __init__(self,name, gender, education, birthday, address, phone, skill, hobbies):
		self.name=name
		self.gender=gender
		self.education=education
		self.birthday=birthday
		self.address=address
		self.phone=phone
		self.skill=skill
		self.hobbies=hobbies
	def WriteFile(self):
		fobj=open('D:\week2\- {}.txt'.format(self.name.upper()), 'w+')
		fobj.write('{}\n'.format(self.name.upper()))
		fobj.write('gender: {}\n'.format(self.gender))
		fobj.write('education: {}\n'.format(self.education))
		fobj.write('birthday: {}\n'.format(self.birthday))
		fobj.write('address: {}\n'.format(self.address))
		fobj.write('phone: {}\n'.format(self.phone))
		fobj.write('skill: {}\n'.format(self.skill))
		fobj.write('hobbies: {}\n'.format(self.hobbies))
		print('{}\n'.format(self.name.upper()))
		fobj.close()
	def Show(self):
		print("Name: ", self.name)
class DSCV:
	hos=['Nguyen','Dinh','Dao','Tran','Le','Ngo','Ho','Doan','Huynh']
	dems=['Thi','Ngoc','Thanh','Van','Minh','Van']
	tens=['Quang','Trang','Tuan','Anh','Duc','Nga','Yen','Hung','Hoa','Tung','Thi']
	gender=['male', 'female']
	education=['Quy Nhon University','Nha Trang University','Phu Yen University','Ha Noi University','Tp. HCM University',
	'Lac Hong University','Nguyen Tat Thanh University','Bach Khoa University','Nong Lam University']
	street=['An Duong Vuong','Hoang Van Thu','Vu Bao','Nguyen Tat Thanh','Dien Hong','Nguyen Thi Dinh']
	district=['Van Canh','Tuy Phuoc','An Nhon','Tay Son','Vinh Thanh','Quy Nhon']
	skill=['Java','Python','PHP','C#','C++']
	hobbies=['fishing','badminton','gym','dance','motor','climbing','music']
	phonesave=[]
	namesaves=[]
	def getnames(self):
		tendaydu=''
		has=1
		while has==1:
			tendaydu=''
			ho=random.sample(self.hos,1)[0]
			dem=random.sample(self.dems,1)[0]
			ten=random.sample(self.tens,1)[0]
			tendaydu=ho+' '+dem+' '+ten
			has=0
			for i in self.namesaves:
				if i==tendaydu:
					has=1
					self.namesaves.append(i)
					break
			if has==0:
				break
		return tendaydu

	def getEducation(self):
		return random.sample(self.education,1)[0]

	def getGender(self):
		return random.sample(self.gender,1)[0]

	def getStreet(self):
		return random.sample(self.street,1)[0]

	def getDistrict(self):
		return random.sample(self.district,1)[0]

	def getDate(self):
		t=datetime.date.today()
		year=random.randint(t.year-25, t.year-20) # lay nam sinh ngau nhien trong khoang 20-25 tuoi
		month=random.randint(1,12)
		if month in [1,3,5,7,8,10,12]:
			day=random.randint(1,31)
		elif month in [4,6,9,11]:
			day=random.randint(1,30)
		else:
			day=random.randint(1,28) 
		return datetime.date(year, month, day)

	def getSkill(self):
		skillget=''
		sk=random.sample(self.skill, random.randint(1,3))
		has=0
		for i in sk:
			newAndExp=i+'({} year)'.format(random.randint(1,10))
			if has==0:
				skillget=skillget + newAndExp
				has=1
			else:
				skillget=skillget + ', '+ newAndExp
		return skillget

	def getHobbies(self):
		hobbiesget=''
		hb=random.sample(self.hobbies, random.randint(1,3))
		has=0
		for i in hb:
			if has==0:
				hobbiesget=hobbiesget + i
				has=1
			else:
				hobbiesget=hobbiesget + ', '+ i
		return hobbiesget 

	def getPhone(self):
		ph=100000000
		has=1
		while has==1:
			ph = random.randint(100000000,999999999)
			has=0
			for i in self.phonesave:
				if i==ph:
					has=1
					self.phonesave.append(i)
					break
			if has==0:
				break
		return '0{}'.format(ph)
		
dscv = DSCV();
for i in range(0,10):
	cv = CV(dscv.getnames(), dscv.getGender(), dscv.getEducation(), dscv.getDate(), dscv.getStreet(), dscv.getPhone(), dscv.getSkill(), dscv.getHobbies())
	cv.WriteFile()