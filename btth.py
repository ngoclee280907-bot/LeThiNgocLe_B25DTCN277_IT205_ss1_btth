import random

print("--------- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---------")

# Nhập thông tin bệnh nhân
name_patient = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính: ")

date_of_birth = int(input("Nhập năm sinh: "))
phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")

exam_fee = float(input("Nhập chi phí khám: "))

# Tạo mã BN tự động
patient_id = 'BN' + str(date_of_birth) + str(random.randint(100, 999))

# Hiển thị thẻ bệnh nhân
print("---------- THẺ BỆNH NHÂN ----------")
print("Mã BN:", patient_id)

print("Tên:", name_patient, "(" + type(name_patient).__name__ + ")")
print("Giới tính:", gender, "(" + type(gender).__name__ + ")")
print("Năm sinh:", date_of_birth, "(" + type(date_of_birth).__name__ + ")")
print("Điện thoại:", phone, "(" + type(phone).__name__ + ")")
print("Email:", email, "(" + type(email).__name__ + ")")
print("Triệu chứng:", symptom, "(" + type(symptom).__name__ + ")")
print("Chi phí:", exam_fee, "VND", "(" + type(exam_fee).__name__ + ")")