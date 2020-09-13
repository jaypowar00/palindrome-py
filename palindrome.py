from os import system
system("cls")
print("To find the next palindrome number!\n")
try:
    n_s = input('Enter any palindrome number : ')
    n = int(n_s)
    l=len(n_s)
    if l%2==0:
        p2 = int(l)-1
        cl= int(l/2) if l!=1 else int(l/2)+1
    else:
        p2 = int(len(n_s))-1
        cl= int(l/2+0.5) if l!=1 else int(l/2)+1
    palindrome = True
    index=None
    for i in range(cl):
        if int(n_s[i])!=int(n_s[p2]):
            print("Given number is not palindrome number!")
            palindrome = False
            break
        else:
            p2-=1
            index=i
    if palindrome:
        print(f"\nGiven number is palindrome")
        next_p=''
        if l%2==0:
            for i in range(int(l/2)):
                next_p+=n_s[i]
            next_p=str(int(next_p)+1)
            next_p+=next_p[::-1]
            print(next_p)
        else:
            for i in range(int(l/2+0.5) if l!=1 else 1):
                next_p+=n_s[i]
            next_p = str(int(next_p)+1)
            next_p += next_p[:index][::-1]
        print(f"The next palindrome number to that of the given palindrome will be:\n{next_p}")
            
        
except:
    if n_s=='':
        print("\nPlease give some input!\n")
    else:
        print("\nSomething went wrong, try again!\n")