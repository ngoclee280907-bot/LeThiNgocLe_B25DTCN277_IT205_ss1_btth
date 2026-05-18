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

print("Tên:", name_patient)
print("Giới tính:", gender)
print("Năm sinh:", date_of_birth)
print("Điện thoại:", phone)
print("Email:", email)
print("Triệu chứng:", symptom)
print("Chi phí:", price, "VND")