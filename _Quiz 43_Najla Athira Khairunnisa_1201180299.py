List_GPA = [2.1 , 2.5 , 4 , 3]

def Function_Bonus (GPA) :
    bonus = 500000
    Function_Bonus = GPA * bonus
    return Function_Bonus

for GPA in List_GPA :
    if GPA > 2.5:
        print("Selamat, anda mendapatkan Rp.", Function_Bonus(GPA))
    else :
        print("Maaf")