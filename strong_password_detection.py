import re

def check_password(password):
    
    check = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')
    output = check.search(password)
    
    if output != None:
        return True
    

if __name__ == "__main__":
        
    password = input("Enter your password : ")
    test = check_password(password)

    if test == True:
        print('Password is strong')

    else:
        print('Please enter strong password')