#class NhanVien(object):
import re
import datetime
import math
import random
def __init__(self, name, gender,education,birthday,address,phone,skill,hobbies):
      self.name = name
      self.gender = gender
      self.education = education
      self.birthday = birthday
      self.address = address
      self.phone = phone
      self.skill = skill 
      self.hobbies = hobbies
# TAO 10 FILE.TXT
fi= ['NGUYEN VAN A','NGUYEN VAN B','NGUYEN VAN C','NGUYEN VAN D','NGUYEN VAN E','NGUYEN VAN F','NGUYEN VAN G','LE VAN A','LE VAN B','LE VAN C']
for f in fi:
  fo = open(f, 'w')
  #KHỞI TẠO VIẾT THÔNG TIN VÀO CÁC FILE
  fo.write('%s' %f)
  gender = ['male','female']
  for w in random.sample(gender,1):
    fo.write ('\ngender: %s' %w)
  education = ['Quy Nhon University','Da Nang University','Ha Noi University','Tp. HCM University','Da Lat University',
  'Sai Gon University','Hai Phong University','Can Tho University','Thai Nguyen University']
  for k in random.sample(education,1):
    print k
  fo.write ('\nEduction: %s' %k)
  d=random.randint(1,31)
  fo.write('\nbirthday:%s'%d)
  t=random.randint(1,12)
  fo.write('-%s'%t)
  y=random.randint(1995,2019)
  fo.write('-%s\n'%y)
  street=['An Duong Vuong','Hoang Hoa Tham','Trung Vuong','Hai Ba Trung','Ton That Thuyet','Quang Trung']
  for t in random.sample(street,1):
    print t
  fo.write ('street: %s' %t)
  district=['An Nhon','Qui Nhon','Tuy Phuoc','Tay Son','An Lao','Phu Cat']
  for d in random.sample(district,1):
    print d
  fo.write (',%s' %d)
  fo.write (",Binh Dinh")
  p=random.randint(1000000000,9999999999)
  fo.write('\nBirthday:%s'%p)
  # phone=[0,1,2,3,4,5,6,7,8,9]
  # phoneget=[]
  # pg=random.sample(phone,7)
  # for p in pg:
  #   phoneget.append(p)
  #   # print p
  # fo.write('\nphone:017%s'%pg)
  skill=['Java','Python','PHP','C#','C++']
  skillget = []
  sg=random.sample(skill,random.randint(1,4))
  for k in sg:
    skillget.append(k)
  fo.write('\nskill: %s' %sg)
  hobbies = ['game','shopping','skiing', 'watches','fishing', 'hunting','cook', 'read books','sailing', 'fashion']
  hobbiesget=[]
  hb=random.sample(hobbies, random.randint(1,3)) 
  for i in hb:
    hobbiesget.append(i)
  fo.write ('\nHobbies: %s' %hb)
fo.close()
    