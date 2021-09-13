def get_password():
    l, u, p, d = 0, 0, 0, 0
    s = str(input('enter your password:'))
    if (len(s) >= 8):
        for i in s:
  
            # counting lowercase alphabets 
            if (i.islower()):
                l+=1            
  
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1            
  
            # counting digits
            if (i.isdigit()):
                d+=1            
  
            # counting the mentioned special characters
            if(i=='#'or i=='$' or i=='%' or i=='&'):
                p+=1           
    if (l>=1 and u>=2 and p>=1 and d>=1 and l+p+u+d==len(s)):
        print("Valid Password")
    else:
        print("Invalid Password")
        
get_password()