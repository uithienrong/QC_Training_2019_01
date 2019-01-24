import datetime
import random
from random import randint


class CV:
  def __init__(self, name, gender, education, birthday, address, phone, skill, hobbies):
    self.name=name
    self.gender=gender
    self.education=education
    self.birthday=birthday
    self.address=address
    self.phone=phone
    self.skill=skill
    self.hobbies=hobbies

name = ['Tran Thi Tam',
        'Le Dinh Thang',
        'Nguyen Thi My Hang',
        'Truong Thi Thu Huong',
        'Le Ngoc Sang',
        'Nguyen Thi Khanh Vy',
        'Dang Thi Thu Thao',
        'Huynh Duy Phat',
        'Nguyen Thanh Trung',
        'Dang Duy Duong',
        'Phan Anh Nguyet',
        'Tran Le Thanh',
        'Nguyen Van Nam',
        'Huynh Thi Nu',
        'Le Viet Trung',
        'Ho Quoc Dat',
        'Tran Kha Nhu']

gender=['male','female']

education=['Quy Nhon University',
           'Nha Trang University',
           'Ha Noi University',
           'Tp. HCM University',
           'Quang Ngai University',
           'Quang Nam University',
           'Hong Bang University',
           'Buon Ma Thuoc University',
           'Da Nang University',
           'Nguyen Tat Thanh University',
           'Quang Trung University']

address=['An Duong Vuong',
         'Ngo May',
         'Le Duan',
         'Tran Hung Dao',
         'Xuan Dieu',
         'Le Loi',
         'Hai Ba Trung']

skill=['.Net',
       'Java',
       'Python',
       'Design',
       'C#',
       'HTML',
       'C++',
       'PHP']

hobbies=['read book',
         'music',
         'soccer',
         'volleyball',
         'web surfing',
         'game',
         'chat']

for i in range(1,11):
    write_text = open('CV' + str(i) +'.txt','w') 

    rand_name = name[random.randint(0,len(name)-1)]
    rand_gender = gender[random.randint(0,len(gender)-1)]
    rand_education = education[random.randint(0,len(education)-1)]
    rand_address = address[random.randint(0,len(address)-1)]
    rand_skill = skill[random.randint(0,round((len(skill)/3)-1))]
    rand_skill_2 = skill[random.randint((round((len(skill)/3)-1)),round((2*len(skill)/3))-1)]
    rand_skill_3 = skill[random.randint(round((2*len(skill)/3)-1),len(skill)-1)]
    rand_hobbies = hobbies[random.randint(0,round((len(hobbies)/2)-1))]
    rand_hobbies_2 = hobbies[random.randint(round((len(hobbies)/2)-1),len(hobbies)-1)]

    lines_of_text = ['Name: ' + rand_name + '\n'
                     + 'Gender: ' + rand_gender + '\n'
                     + 'Education: ' + rand_education + '\n'
                     + 'Birthday: ' + str(randint(1,28)) + '/' + str(randint(1,12)) + '/' + str(randint(1994,1999)) + '\n'
                     + 'Address: ' +  str(randint(1,200)) + ' ' + rand_address + '\n'
                     + 'Phone: ' + '09' + str(random.randint(10000000,99999999)) + '\n'
                     + 'Skill: ' + rand_skill + ' (' + str(random.randint(0,5)) + ' year)' + ', '
                     + rand_skill_2 + ' (' + str(random.randint(1,6)) + ' year)' + ', '
                     + rand_skill_3 + ' (' + str(random.randint(1,6)) + ' year)'+ '\n'
                     + 'Hobbies: ' + rand_hobbies + ', ' + rand_hobbies_2 + '\n'] 
    write_text.writelines(lines_of_text) 
    write_text.close()