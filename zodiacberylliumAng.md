def birthYear():
    userbirthYear = int(input("Enter your birth year: "))
    if userbirthYear < 1900:
        print("Invalid year, your birth year must be after 1900")
    else:
        return userbirthYear

def chineseZodiac(userbirthYear):
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    zodiacIndex = (userbirthYear - 1900) % 12
    print(f"Your Chinese Zodiac Sign is : {zodiac[zodiacIndex]}")

def main():  
    userbirthYear = birthYear()
    if userbirthYear is not None:
        chineseZodiac(userbirthYear)

main()
