#"program to output day name by inputting month and date from user"
# Check the day of the month by giving date
m=input("""Enter month name without 'mistake':""")
d=int(input("Enter date of the month:"))
if (m=="january" or m=="January" or m=="April" or m=="april" or m=="july" or m=="July"):
    if (m=="january" or m=="January") and (d<=31 and d>0):
        i=(2+d)%7
        if (d==12) and (i==0):
            print("Sunday")
            print("On this day")
            print("Birth of Swamivevekanada")
            print("National Youth Day")
        elif (d==26) and (i==0):
            print("Sunday")
            print("On this day")
            print("Republic Day")
        elif (d==1) and (i==3):
            print("Wednesday")
            print("On this day")
            print("New Year'S Day")
        elif (d==25) and (i==6):
            print("Saturday")
            print("On this day")
            print("National Voters Day")
        elif (d==28) and (i==2):
            print("Tuesday")
            print("On this day")
            print("Birth of Lal Bahadhur Sashri")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
        else:
            print("Invalid date enter proper date")
            
    elif (m=="april" or m=="April") and (d<=30 and d>0):
        i=(2+d)%7
        if (d==1) and (i==0):
            print("Sunday")
            print("On this day ")
            print("April Fool's Day")
        elif (d==7) and (i==2):
            print("Tuesday")
            print("On this day")
            print("World Health Day")
        elif (d==10) and (i==5):
            print("Friday")
            print("On this day")
            print("Good Friday")
        elif (d==13) and (i==1):
            print("Monday")
            print("On this day")
            print("Vaisaki")
        elif (d==14) and (i==2):
            print("Tuesday")
            print("On this day")
            print("Ambedkar Jayanthi")
        elif (d==18) and (i==6):
            print("Saturday")
            print("On this day")
            print("World Heritage Day")
        elif (d==21) and (i==2):
            print("Tuesday")
            print("On this day")
            print("World creativity and Innovation Day")
        elif (d==22) and (i==3):
            print("Wednesday")
            print("On this day")
            print("World Earth Day")
        elif (d==29) and (i==3):
            print("Wednesday")
            print("On this day")
            print("International Dance Day")
        elif (i==4) and (d==2):
            print("Thrusday")
            print("On this day ")
            print("Ram Navami")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
        else:
            print("Invalid date enter proper date")
            
    elif (m=="july" or m=="July") and(d<=31 and d>0):
        i=(2+d)%7
        if (d==1) and (i==3):
            print("Wednesday")
            print("On this day")
            print("Doctor's Day")
        elif (d==11) and (i==6):
            print("Saturday")
            print("On this day")
            print("World Population Day")
        elif (d==29) and (i==3):
            print("Wednesday")
            print("On this day")
            print("International Tigers Day")
        elif (d==28) and (i==2):
            print("Tuesday")
            print("On this day")
            print("World Nature Conservation Day")
        elif (d==3) and (i==5):
            print("Friday")
            print("On this day")
            print("Plastic Bag Free Day")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
        
elif (m=="February" or m=="february" or m=="august" or m=="August"):
    if (m=="February" or m=="february") and (d<=29 and d>0):
        i=(5+d)%7
        if (d==4) and (i==2):
            print("Tuesday")
            print("On this day")
            print("World Cancer Day")
        elif (d==14) and (i==5):
            print("Friday")
            print("On this day")
            print("Valentine's Day")
        elif (d==22) and (i==6):
            print("Saturday")
            print("On this day")
            print("World Scout Day")
        elif (d==28) and (i==5):
            print("Friday")
            print("On this day")
            print("National Science Day")
        elif (d==19) and (i==2):
            print("Tuesday")
            print("On this Day")
            print("Shivaji Jayanthi")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
        else:
            print("Invalid date enter proper date")
            
    elif (d<=31and d>0):
        i=(5+d)%7
        if (d==4) and (i==2):
            print("Tuesday")
            print("On this day")
            print("FriendShip Day")
        elif (d==15) and (i==6):
            print("Friday")
            print("On this  day")
            print("INDIA'S Independence DAY")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
elif (m=="March" or m=="march" or m=="november" or m=="November"):
    if (m=="november" or m=="November") and (d<=30 and d>0):
        i=(6+d)%7
        if (d==14 and i==6):
            print("Saturday")
            print("On this day")
            print("Children'S Day")
        elif (d==5 and i==4):
            print("Thrusday")
            print("On this day")
            print("World Tsunami Day")
        elif (d==7 and i==6):
            print("Saturday")
            print("On this day")
            print("National Cancer Awareness Day")
        elif (d==21 and i==6):
            print('Saturday')
            print("On this day")
            print("World Television Day")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
        else:
            print("Invalid date enter proper date")
    elif (m=="March" or m=="march") and (d<32 and d>0):
        i=(5+d)%7
        if (d==1 and i==0):
            print("Sunday")
            print("On this day")
            print("Zero Discrimination day")
        elif (d==3 and i==2):
            print("Tuesday")
            print("On this day")
            print("World WildLife Day")
        elif (d==8 and i==0):
            print("Sunday")
            print("On this day")
            print("International Women's Day")
        elif (d==14 and i==6):
            print('Saturday')
            print("On this day")
            print("1.PI Day")
            print("2.Albert Einstein Birthday")
        elif (d==20 and i==5):
            print("Friday")
            print("On this day")
            print("1.International Day of Happiness")
            print("2.World Sparrow Day")
        elif (d==21  and i==6):
            print("Saturday")
            print("On this day")
            print("World Forestry Day")
        elif (d==22 and i==0):
            print("Sunday")
            print("On this day")
            print("World Water Day")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
elif (m=="may" or m=="May"):
    if (d<32 and d>0):
        i=(4+d)%7
        if (d==1 and i==5):
            print("Friday")
            print("On this day")
            print("International Labour's Day")
        elif (d==3 and i==0):
            print("Sunday")
            print("On this day")
            print("World Laughter Day")
        elif (d==7 and i==4):
            print("Thrusday")
            print("On this day")
            print("Wolrd Athletic's Day")
        elif (d==17 and i==0):
            print("Sunday")
            print("On this day")
            print("World Telecommunication Day")
        elif (d==22 and i==5):
            print("Friday")
            print("On this day")
            print("International Day for Biological and Diversity")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
elif (m=="June" or m=="june"):
    if (d<31 and d>0):
        i=(0+d)%7
        if (d==2 and i==1):
            print("Monday")
            print("On this day")
            print("Telangana Formation Day")
        elif (d==3 and i==3):
            print("Wednesday")
            print('On this day')
            print("World Bicycle Day")
        elif (d==5 and i==5):
            print("Friday")
            print("On this Day")
            print("World Environment Day")
        elif (d==8 and i==1):
            print("Monday")
            print("On this Day")
            print("1.World Ocean Day"
                  "\n2.World Brain Tumor Day"
                  "\n3.Ajay's Bornday")
        elif (d==12 and i==5):
            print("Friday")
            print("On this day")
            print("Anti-Child Labour Day")
        elif (d==14 and i==0):
            print("Sunday")
            print("On this day")
            print("World Blood Donor Day")
        elif (d==15 and i==1):
            print("Monday")
            print("on this day")
            print("World Wind Day")
        elif (d==21 and i==0):
            print("Sunday")
            print("On this day")
            print("International Day of Yoga")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
elif (m=="September" or m=="september" or m=="December" or m=="december"):
    if (m=="september" or m=="September") and (d<31 and d>0):
        i=(1+d)%7
        if (d==5 and i==6):
            print("Saturday")
            print("On this day")
            print("Teacher's Day")
        elif (d==8 and i==2):
            print("Tuesday")
            print("On this day")
            print("International Literacy Day")
        elif (d==14 and i==1):
            print("Monday")
            print("On this day")
            print("Hindi Divas")
        elif (d==15 and i==2):
            print("Tuesday")
            print("On this day")
            print("Engineer's Day")
        elif (d==16 and i==3):
            print("Wednesday")
            print("On this day")
            print("World Ozone Day")
        elif (d==29 and i==2):
            print("Tuesday")
            print("On this day")
            print("World Heart Day")
        elif (d==30 and i==3):
            print("Wednesday")
            print("On this day")
            print("World Translation Day")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
        else:
            print("Invalid date enter proper date")
    elif (m=="december" or m=="December") and (d<=31 and d>0):
        i=(1+d)%7
        if (d==1 and i==2):
            print("Tuesday")
            print("On this day")
            print("World AID'S Day")
        elif (d==2 and i==3):
            print("Wednesday")
            print("On this day")
            print("National Pollution Control Day")
        elif (d==3 and i==4):
            print("Thrusday")
            print("On this day")
            print("World Day of the Handicapped")
        elif (d==4 and i==5):
            print("Friday")
            print("On this day")
            print("Indian Navy Day")
        elif (d==10 and i==4):
            print("Thrusday")
            print("On this day")
            print("Human Right's Day")
        elif (d==14 and i==1):
            print("Monday")
            print("On this day")
            print("World Energy Conservation Day")
        elif (d==22 and i==2):
            print('Tuesday')
            print("On this day")
            print("Mathematics day and Ramanujan Birthday")
        elif (d==23 and i==3):
            print("Wednesday")
            print("On this day")
            print("Farmer's Day")
        elif (d==25 and i==5):
            print("Friday")
            print("On this day")
            print("Christmas Day")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
elif (m=="October" or m=="october"):
    if (d<=31 and d>0):
        i=(3+d)%7
        if (d==2 and i==5):
            print("Friday")
            print("On this day")
            print("Non-Violence Day")
        elif (d==4 and i==0):
            print("Sunday")
            print("On this day")
            print("World Animal Welfare Day")
        elif (d==15 and i==4):
            print("Thrusday")
            print("On this day")
            print("World Students Day")
        elif (d==16 and i==5):
            print("Friday")
            print("On this day")
            print("World Food Day")
        elif (d==31 and i==6):
            print("Saturday")
            print("On this day")
            print("World Unity Day")
        elif (i == 0):
            print("Sunday")
        elif (i == 1):
            print("Monday")
        elif (i == 2):
            print("Tuesday")
        elif (i == 3):
            print("Wednesday")
        elif (i == 4):
            print("Thrusday")
        elif (i == 5):
            print("Friday")
        elif (i == 6):
            print("Saturday")
    else:
        print("Invalid date enter proper date")
else:
    print("Invalid month name check your month spelling")
print("***WEL-COME TO CALENDAR 2020***")






