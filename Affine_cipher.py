#This program is designed to encode and decode the mesasage using Affine cipher:
def encode(msg,a,b):
    '''
    Purpose:- This function is desined to encode the given message.
    Input:-   msg:takes string value as an input.
    Output:-  Returns encoded message.
    e.g.:-
            I/P: msg = Hello My Name , a = 3, b = 3
            O/P: Ypkkt Nx Qdnp
    '''
    ecd=""                             
    for i in msg:
        if(i.islower()):
            ecd += chr(((a*(ord(i)-97))+b) % (26)+97)    #converting character to ascii value then performing (P+K) mod 26 to encode the msg.
        elif(i.isupper()):
            ecd += chr(((a*(ord(i)-65))+b) % (26)+65)
        else:
            ecd += i

    return ecd

  

def decode(msg,a,b):
    '''
    Purpose:- This function is desined to decode the given message.
    Input:-   msg:takes string value as an input.
    Output:-  Returns decoded message.
    e.g.:-
            I/P: msg = Ypkkt Nx Qdnp , a = 3, b = 3
            O/P: Hello My Name
    '''
    if(mod_inverse(a,26)==None):
        return None
    dcd=""                                 
    for i in msg:
        if(i.islower()):
            dcd += chr(((mod_inverse(a,26))*(ord(i)-97-b) % 26)+97)    #converting character to ascii value then performing (P-K) mod 26 to decode the msg.
        elif(i.isupper()):
            dcd += chr(((mod_inverse(a,26))*(ord(i)-65-b) % 26)+65)
        else:
            dcd += i
        
    return dcd    

def mod_inverse(a,b):                          
    for i in range(1,b):
        flag = (a*i) % b
        if flag == 1:
            return i
    return None



def main():
    '''
    Driver code
    '''
    msg=input("Enter the message to encode : ")  
    a = int(input("Enter the number: "))        
    b = int(input("Enter the number: "))
    en=encode(msg,a,b)                                       
    print("The message you entered:",msg)                
    print("The message after encoding :",en) 
    if(decode(en,a,b) == None):
        print("Sorry!! This message can not be decoded.")
    else:            
        print("The message after decoding it :",decode(en,a,b))  
    
if __name__=='__main__':
    main()      #calling main() function.