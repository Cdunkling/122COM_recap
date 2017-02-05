import sys
import re

def find_type(value):
    if value.lower()=="true" or value.lower()=="false":
        return "boolean"
    searchstr = re.search( r'[A-Za-z]', value)
    searchint = re.match( r'[0-9]', value)
    if(searchstr):
        return "string"
    elif(searchint and list(value).count('.')==0):
        return "int"
    elif(list(value).count('.')==1):
       return "float"
    else:
        return "string"

def main():
    print('Enter something to identify if it\'s an int, float, string or boolean')
    val=input("val: ")
    find_type(val)

















def testing():
    tests = [('1','int'),('1.23','float'),('hello','string'),('True','boolean'),('1.2.3.4','string'),('fAlSe','boolean'),('fa1se','string'),('this is true','string')]

    errors = 0
    for test, correctAnswer in tests:
        yourAnswer = find_type(test)

        if correctAnswer != yourAnswer:
            print('Error! {} is a {} but find_type() claims it is a {}'.format(test,correctAnswer,yourAnswer))
            print()
            errors += 1

    if errors == 0:
        print('Congratulations, no errors')
    else:
        print('Uh oh, {} error/s remain'.format(errors) )
        
    return errors

if __name__ == '__main__':
    errors = testing()
    main()
    sys.exit(errors)
