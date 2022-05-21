#Menghitung BMI
print("Menghitung Body Mass Index (BMI)")
Tinggi = float(input("Masukan Tinggi Anda (meter) :"))
BB = int(input("Masukan Berat Badan Anda (kg) : "))
BMI = BB/(Tinggi*Tinggi)
if BMI < 18 :
    print("BMI = ", BMI,", Berat badan anda kurang")
elif BMI >=18.5 and BMI <=25 :
    print("BMI = ",BMI, ", Berat badan anda normal")
elif BMI>25 :
    print("BMI = ",BMI, ", Berat Badan anda berlebih")
