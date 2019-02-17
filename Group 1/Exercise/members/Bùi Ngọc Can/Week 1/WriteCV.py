import datetime
import random

# Class ung vien
class Ungvien:
	#phuong thuc khoi tao
	def __init__(self, name, gender, education, birthday, address, phone, skill, hobbies):
		self.name=name
		self.gender=gender
		self.education=education
		self.birthday=birthday
		self.address=address
		self.phone=phone
		self.skill=skill
		self.hobbies=hobbies

#cac mang chua gia tri random
names=['Nguyen Van A','Le Thi B','Do Tran C','Nguyen Thi D','Le Trung E','Bui Ta F','Ho Minh G','Nguyen Tuan H','Le Van I', 'Do Quoc J','Ho Tan K','Le Quoc L','Tran Thien M','Vo Thien N']
gender=['male', 'female']
education=['Quy Nhon University','Da Nang University','Ha Noi University','Tp. HCM University','Da Lat University',
	'Sai Gon University','Hai Phong University','Can Tho University','Thai Nguyen University']
street=['An Duong Vuong','Hoang Hoa Tham','Trung Vuong','Hai Ba Trung','Ton That Thuyet','Quang Trung']
district=['An Nhon','Qui Nhon','Tuy Phuoc','Tay Son','An Lao','Phu Cat']
skill=['Java','Python','PHP','C#','C++']
hobbies=['music','badminton','gym','dance','football','motor','climbing']	

#function lay ngay sinh 
def getDate():
	t=datetime.date.today()
	year=random.randint(t.year-25, t.year-20) # lay nam sinh ngau nhien trong khoang 20-25 tuoi
	month=random.randint(1,12)
	if month in [1,3,5,7,8,10,12]:
		day=random.randint(1,31)
	elif month in [4,6,9,11]:
		day=random.randint(1,30)
	else:
		day=random.randint(1,28) 
	#o day ta khong tinh truong hop nam nhuan
	return datetime.date(year, month, day)

#function lay skill
def getSkill():
	skillget=[]
	sk=random.sample(skill, random.randint(1,3)) # lay ngau nhien skill voi so luong tu 1-3
	for i in sk:
		newAndExp=i+'({} year)'.format(random.randint(1,10)) # voi moi skill, them so nam kinh nghiem tu 1-0 nam
		skillget.append(newAndExp)
	return skillget

#function lay hobbies
def getHobbies():
	hobbiesget=[]
	hb=random.sample(hobbies, random.randint(1,3)) # lay ngau nhien hobbies voi so luong tu 1-3
	for i in hb:
		hobbiesget.append(i)
	return hobbiesget

#lay ngau nhien 10 ten t list names cho truoc o tren
usingname=random.sample(names,10)

#ham ghi file
def writeFile():
	for i in usingname:
	#khoi tao Ungvien
		ungvien=Ungvien(i, 
			random.choice(gender), #lay ngau nhieu gioi tinh male hoac female
		 	random.choice(education), # lay ngau nhien education tu list education o tren
		  	getDate(), # goi ham getDate() de lay ngay sinh ngau nhien
			'{} {}, {}, {}'.format(random.randint(1,100), random.choice(street), random.choice(district), 'Binh Dinh'), #lay ngau nhien so nha tu 1-100,
			 #ten duong, quan huyen ngau nhien tu list cho truoc, tinh de mac dinh la Binh Dinh
			'0{}'.format(random.randint(100000000,999999999)), #lay ngau nhien 9 so sau cua so dien thoai tu 100000000-999999999
			getSkill(), getHobbies()) 
		
		chuoiskill=''
		for j in ungvien.skill:
			chuoiskill=chuoiskill+' {},'.format(j) # tao chuoi cac skill de in ra
		chuoiskill = chuoiskill.rstrip(',')

		chuoihobbies=''
		for j in ungvien.hobbies:
			chuoihobbies=chuoihobbies+' {},'.format(j, random.randint(1,10)) # tao chuoi cac hobbies de in ra
		chuoihobbies = chuoihobbies.rstrip(',')

		fobj=open('CV - {}.txt'.format(i.upper()), 'w')
		fobj.write('{}\n'.format(i.upper()))
		fobj.write('gender: {}\n'.format(ungvien.gender))
		fobj.write('education: {}\n'.format(ungvien.education))
		fobj.write('birthday: {}\n'.format(ungvien.birthday))
		fobj.write('address: {}\n'.format(ungvien.address))
		fobj.write('phone: {}\n'.format(ungvien.phone))
		fobj.write('skill: {}\n'.format(chuoiskill))
		fobj.write('hobbies: {}\n'.format(chuoihobbies))

#ham main
def main():
	writeFile()

#goi ham main
main()


	



