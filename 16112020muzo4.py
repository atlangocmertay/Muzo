x = float(input("Please enter your score: "))
y = x / 100
if 0 <= y < 0.6:
    print("Your Grade is F")
elif 0.6 <= y < 0.7:
    print("Your Grade is D")
elif 0.7 <= y < 0.8:
    print("Your Grade is C")
elif 0.8 <= y < 0.9:
    print("Your Grade is B")
elif 0.9 <= y <= 1.0:
    print("Your Grade is A")
else:
    print("Düzgün sayı giriniz beyefendi oha amk")
