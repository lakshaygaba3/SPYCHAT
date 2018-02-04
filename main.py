from spy_detail import spy_name, spy_rating, spy_salutation, spy_age

print "hello world"
print  "let's get started"

def start_chat(spy_name,spy_age, spy_rating):
    menu_choice = input("What do you want to do? \n 1. Add a status update \n 0. Close application")
    show_menu = True
    while show_menu:
        if menu_choice == 1:
            spy_status = raw_input("Write a status update")
            print "your status is %s" % spy_status
        elif menu_choice == 0:
            show_menu = False
        else:
            show_menu = False
            print "Invalid choice"


existing = raw_input("Continue as " + spy_salutation + " " + spy_name + "(Y/N)?")
if existing.upper() == "Y":
      #Continue with the default user/details imported from the helper file.
    print "Welcome %s %s age: %d Rating: %.1f Glad to have you back." % (spy_salutation,spy_name,spy_age,spy_rating)
    start_chat(spy_name,spy_age,spy_rating)

elif existing.upper() == "N":
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name)>3:
        print "welcome " + spy_name + " glad to meet you."
        spy_salutation =raw_input("what should i cal you ? mr. or ms. ")
        spy_name = spy_salutation + " " +spy_name
        print spy_name
        print "alright" + " " + " " + spy_name + " " + "i'd like to know a little more about u"
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_age = input("what is your age? ")
        if spy_age>12 or spy_age<50:
            print "spy, your age is perfect"
            spy_rating = input("what is your rating? ")
            if spy_rating >=5.0:
                print "Great spy"
            elif spy_rating<5.0 and spy_rating>=4.5:
                print "nice spy"
            elif spy_rating<4.5 and spy_rating>=3.5:
                print "fine spy"
            else:
                print "fuck off"
            spy_is_online = True
            print "Authentication complete. Welcome  %s age: %d and rating of: %.1f Proud to have you onboard" % (spy_name, spy_age, spy_rating)



        else:
            print "your age is not valid to be a spy"
    else:
        print "please enter a valid name of atleast 4 letter"
else:
     print "invalid responce"
