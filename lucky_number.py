#to check if a given number is Lucky (all digits are different)
def is_lucky(number):
    lst={}
    for key,val in (enumerate(str(number))):
        if val in lst:
            return False
        else:
            lst[val]=1
    return True
   


print(is_lucky(123456789))

