import random


database = {}

def init():

    import datetime
    print("Welcome to HorlarBank")

    print("=== ==== ====== ==== ====================")
    datetime_object = datetime.datetime.now()
    
    print(datetime_object)
    print("=== ==== ====== ==== ====================")

    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("********* Enter Your Login Details ********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password: \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                #isLoginSuccessful = True
        else:
            print("Invalid Login Details")
    login()

    

def register():

    print("****** Sign Up Here *******")

    email = input("Enter email address: \n")
    first_name =  input("Enter your first name? \n")
    last_name =  input("Enter your last name? \n")
    password = input("Create a password: \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password]

    print("Your Account has been created")
    print("=== ==== ====== ==== ===")
    print("Your account number is: %d" %accountNumber)
    print("=== ==== ====== ==== ====================")
    print("DISCLAIMER : Do not share your details with anyone")
    print("=== ==== ====== ==== ===")

    login()


def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do?: (1) Deposit (2) Withdarwal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        depositOpration()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        Logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(user)

def withdrawalOperation():
    input("How much would you like to withdraw: \n")
    print('Take Your Cash')

def depositOpration():
    amount = input("How much would you like to deposit \n")
    print('Current Balance : %s' % amount)



def generationAccountNumber():
    
    return random.randrange(111111,999999)

def Logout():
    print("       ")
    print("THANK YOU FOR BANKING WITH US")
    login()

init()
