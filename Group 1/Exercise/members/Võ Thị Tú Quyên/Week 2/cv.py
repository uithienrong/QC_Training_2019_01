import random
import datetime

class Cv:
    def __init__(self, name, gender, education, birthday, address, phone, skill, hobbies):
        self.name = name
        self.gender = gender
        self.education = education
        self.birthday = birthday
        self.address = address
        self.phone = phone
        self.skill = skill
        self.hobbies = hobbies

name = ('Nguyen Cong Phuong','Dang Van Lam','Que Ngoc Hai','Bui Tien Dung','Dang Van Hau','Do Duy Manh','Luong Xuan Truong','Nguyen Quang Hai','Nguyen Trong Hoang','Ha Duc Chinh')
gender = ('male','female') # Sử dụng Tuple tiêu hao bộ nhớ ít hơn List, nên hiệu xuất sẽ tốt hơn
edu = ('Quy Nhon University',' Binh Dinh Colleges','Can Tho University','Tp. HCM University','Quang Trung University','Dong A University','Duy Tan University','Lac Hong University','Da Nang University','Nguyen Tat Thanh University','HUTECH University')
street = ('An Duong Vuong','Le Hong Phong','Thanh Nien','Hoang Van Thu','Xuan Dieu','Le Lai','Le Thanh Ton')
district = ('An Nhon','Qui Nhon','Tuy Phuoc','Tay Son','An Lao','Phu Cat')
skill = ['C#','C/C++','Java','Python','Ruby','Go','WPF','JS']
hobbies = ('sing','music','soccer','volleyball','play chess','cooking','rowing')
phone = (1,2,3,4,5,6,7,8,9)

def getPhone(): # Lấy số điện thoại, yêu cầu ngẫu nhiên 10 số nguyên bất kì, mọi số điện thoại đều bắt đầu bằng số 0
    numphone = '0'
    for i in range(9):
        b = random.choice(phone)
        b = str(b)
        numphone += b
    return numphone

def getGender(): # Chọn giới tính
    return random.choice(gender)

def getEdu():
    return random.choice(edu)

def getHob(): #Sở thích lấy ngẫu nhiên từ 1-3
    needreturn = ''
    s = ', '
    hb = random.sample(hobbies,random.randint(1,3))
    # Đưa sở thích sang dạng chuỗi
    needreturn = s.join(hb)
    return needreturn

def getDate(): # lấy ngày sinh
    t = datetime.date.today()
    nam = random.randint(t.year-25, t.year-20) # lấy nắm sinh ngẫu nhiên từ 20 - 25
    month = random.randint(1,12)
    if month in [1,3,5,7,8,10,12]:
        day=random.randint(1,31)
    elif month in [4,6,9,11]:
        day=random.randint(1,30)
    else:
        day=random.randint(1,28) 
	# Không tính năm nhuận
    return datetime.date(nam, month, day).strftime('%d/%m/%Y') # Định dạng ngày tháng theo dd/m/yy

def getSkill():
    needreturn = []
    s = ', '
    sk = random.sample(skill,random.randint(1,3)) # Lấy ngẫu nhiên 1-3 skill
    for i in sk:
        exp = str(random.randint(1,10)) + ' nam' # Số năm kinh nghiệm từ 1-10 năm
        skillAndexp = i + ' ({})'.format(exp)
        needreturn.append(skillAndexp)
    return s.join(needreturn)

def getAddr():
    num = (0,1,2,3,4,5,6,7,8,9)
    lsoNha = random.sample(num,3) # Lấy ngẫu nhiên số nhà, tối đa 3
    soNha = ''
    for i in lsoNha:
        soNha += str(i)
    duong = random.choice(street) # Chọn đường
    huyen = random.choice(district) # CHọn Huyện
    return soNha+' '+duong+', '+huyen+', '+'Binh Dinh'

tenCV = random.sample(name,10)

for i in tenCV:
    # Khởi tạo đối tượng
    cv = Cv(
        i,
        getGender(),
        getEdu(),
        getDate(),
        getAddr(),
        getPhone(),
        getSkill(),
        getHob()
    )

    with open('CV - {}.txt'.format(i.upper()),'w') as fileCV:
        fileCV.write('{}\n'.format(cv.name))
        fileCV.write('Gender: {}\n'.format(cv.gender))
        fileCV.write('Education: {}\n'.format(cv.education))
        fileCV.write('Birthday: {}\n'.format(cv.birthday))
        fileCV.write('Address: {}\n'.format(cv.address))
        fileCV.write('Phone: {}\n'.format(cv.phone))
        fileCV.write('Skill: {}\n'.format(cv.skill))
        fileCV.write('Hobbies: {}\n'.format(cv.hobbies))

