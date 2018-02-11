from spy_detail import spy

print "hello world"
print "let's get started"
STATUS_MESSAGES = ['JAMES BOND 007', 'JAGGA JASOOS', 'BYOKSHI', 'TUMSE NA HOGA SPY']
friends = [{'name' : 'jatin', 'age' :25, 'rating' :5, 'is_online' :True},{'name': 'naveen', 'age' :28, 'rating':4, 'is_online':True}]


def add_status(C_S_M):
    if C_S_M != None:
        print "your current status is " + C_S_M
    else:
        print "you don't have any status"

    user_choise = raw_input("do you want to select from old status? Y or N: ")

    if user_choise.upper() == 'Y':
        serial_no = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1

        user_status_selection = input("Which one do u want to set this time? ")
        new_status = STATUS_MESSAGES[user_status_selection - 1]

    elif user_choise.upper() == 'N':
        new_status = raw_input("write your status")
        STATUS_MESSAGES.append(new_status)
    else:
        print "invalid entry"
    return new_status

def add_friend():
    frnd = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    frnd['name'] = raw_input("write your frnd's name: ")
    frnd_sal = raw_input("Mr. or Mrs. :")
    frnd['name'] = frnd_sal + " " + frnd['name']
    frnd['age'] = input("what's ur frnd age :")
    frnd['rating'] = input("write your frnd rating :")

    if len(frnd['name'])>2 and 50>=frnd['age']>=12 and frnd['rating'] >=spy['rating']:
        friends.append(frnd)
    else:
        print "frnd with these value can't be added"
    return len(friends)

def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input(
            "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 0. Close application")
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print "your new status is updated to" + updated_status_message
        elif menu_choice == 2:
            no_of_frnds = add_friend()
            print "i have " + str(no_of_frnds) + " friends"
        elif menu_choice == 0:
            show_menu = False
        else:
            show_menu = False
            print "Invalid choice"


existing = raw_input("Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?")
if existing.upper() == "Y":
    # Continue with the default user/details imported from the helper file.
    print "Welcome %s %s age: %d Rating: %.1f Glad to have you back." % (spy['salutation'], spy['name'], spy['age'], spy['rating'])
    start_chat(spy['name'], spy['age'], spy['rating'])

elif existing.upper() == "N":
    spy = {
        'name': '',
        'salutation': 'Mr.',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 3:
        print "welcome " + spy['name'] + " glad to meet you."
        spy_salutation = raw_input("what should i cal you ? mr. or ms. ")
        spy['name'] = spy_salutation + " " + spy['name']
        print spy['name']
        print "alright" + " " + " " + spy['name'] + " " + "i'd like to know a little more about u"
        spy['age'] = input("what is your age? ")
        if spy['age'] > 12 or spy['age'] < 50:
            print "spy, your age is perfect"
            spy['rating'] = input("what is your rating? ")
            if spy['rating'] >= 5.0:
                print "Great spy"
            elif spy['rating'] < 5.0 and spy['rating'] >= 4.5:
                print "nice spy"
            elif spy['rating'] < 4.5 and spy['rating'] >= 3.5:
                print "fine spy"
            else:
                print "fuck off"
            spy_is_online = True
            print "Authentication complete. Welcome  %s age: %d and rating of: %.1f Proud to have you onboard" % (
                spy['name'], spy['age'], spy['rating'])



        else:
            print "your age is not valid to be a spy"
    else:
        print "please enter a valid name of atleast 4 letter"
else:
    print "invalid responce"
