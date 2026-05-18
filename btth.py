import random

print("--------- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---------")

# Nhập thông tin bệnh nhân
name_patient = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính: ")

date_of_birth = int(input("Nhập năm sinh: "))
phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")

price= float(input("Nhập chi phí khám: "))

# Tạo mã BN tự động
patient_id = 'BN' + str(date_of_birth) + str(random.randint(100, 999))

# Hiển thị thẻ bệnh nhân
print("---------- THẺ BỆNH NHÂN ----------")
print("Mã BN:", patient_id)

print("Tên:", type(name_patient))
print("Giới tính:", type(gender))
print("Năm sinh:", type(date_of_birth))
print("Điện thoại:", type(phone))
print("Email:", type(email))
print("Triệu chứng:", type(symptom))
print("Chi phí:", type(price))