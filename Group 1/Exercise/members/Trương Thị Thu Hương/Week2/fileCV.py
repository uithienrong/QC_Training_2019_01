import random
class NhanVien:
	def __init__(self, name, gender, education, address, phone, skill, hobbies, day, month, year):
		self.name=name
		self.gender=gender
		self.education=education
		self.address=address
		self.phone=phone
		self.skill=skill
		self.hobbies=hobbies
		self.day=day
		self.month=month
		self.year=year
name=['NGUYEN VAN A','NGUYEN VAN B','NGUYEN VAN C','NGUYEN VAN D','NGUYEN VAN E','NGUYEN VAN F','NGUYEN VAN G','LE VAN A','LE VAN B','LE VAN C']
gender=['male', 'female']
education=['Quy Nhon University','Da Nang University','Ha Noi University','Tp. HCM University','Da Lat University',
  'Sai Gon University','Hai Phong University','Can Tho University','Thai Nguyen University']
street=['An Duong Vuong','Hoang Hoa Tham','Trung Vuong','Hai Ba Trung','Ton That Thuyet','Quang Trung']
district=['Dieu Tri','Qui Nhon','Tuy Phuoc','Tay Son','Phu My','Phu Cat']
skill=['C','Java','Ruby','HTML','Python','C#','PHP','C++']
hobbies=['music','badminton','chess','dance','football','volleyball','tenis']

def getgender():
	return random.choice(gender)
def geteducation():
	return random.choice(education)
def getaddress():
	getaddress=[]
	address=random.choice(street) +', '+ random.choice(district)
	getaddress.append(address)
	print address
	return getaddress
def getday():
	getday=[]
	day=str(random.randint(1,31))
	getday.append(day)
	print day
	return getday
def getmonth():
	getmonth=[]
	month=str(random.randint(1,12))
	getmonth.append(month)
	print month
	return getmonth
def getyear():
	getyear=[]
	year=str(random.randint(1994,2019))
	getyear.append(year)
	print year
	return getyear
def getphone():
	getphone=[]
	phone=str(random.randint(100000000,999999999))
	getphone.append(phone)
	print phone
	return getphone
def gethobbies():
	gethobbies=[]
	hobb=random.sample(hobbies, random.randint(1,3))
	for i in hobb:
		gethobbies.append(i)
		print i
	return gethobbies
def getskill():
	getskill=[]
	skill1=random.sample(skill, random.randint(1,4))
	for i in skill1:
		getskill.append(i)
		print i
	return getskill
def main():
	name1=random.sample(name,10)
	for i in name1:
		name1=NhanVien(i,getgender(),geteducation(),getaddress(),getphone(), getskill(), gethobbies(), getday(), getmonth(),getyear())
		file=open(i+'.txt', 'w')
		file.write('%s\n'%i)
		file.write('gender: %s\n'%getgender())
		file.write('education:%s \n'%geteducation())
		file.write('Birthay:%s'% (', '.join(name1.day)))
		file.write('-%s'%(', '.join(name1.month)))
		file.write('-%s\n'%(', '.join(name1.year)))
		file.write('address: %s'%(', '.join(name1.address) )+',Binh Dinh \n')
		file.write('phone: %s\n'%(', '.join(name1.phone) ))
		file.write('skill:%s\n'%(', '.join(name1.skill)))
		file.write('hobbies:%s\n'%(', '.join(name1.hobbies)))
		file.close();

main()
