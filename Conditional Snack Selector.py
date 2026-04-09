age = int(input("What is your age?"))
hascoupon = input("Do you have a coupon? yes or no?")
hasmoney = input("Do you have money? yes or no?")
snacks = []
if age < 12 or hascoupon == "yes":
    snacks.append("cotton candy")
if age >= 10 and hasmoney == "yes":
    snacks.append("popcorn")
if hascoupon == "yes" or hasmoney == "yes":
    snacks.append("ice cream")
if snacks:
    print(snacks)
    print(snacks[0])
    if len(snacks)>=2:
        print(snacks[1])

    if len(snacks)==3:
        print(snacks[2])
else:
    print("Sorry,no snacks for you")

