#This program is designed to encode and decode the mesasage using Additive cipher:
def encode(msg,k):
    '''
    Purpose:- This function is desined to encode the given message.
    Input:-   msg:takes string value as an input.
    Output:-  Returns encoded message.
    e.g.:-
            I/P: msg = ABCD 123 , k = 2
            O/P: CDEF 123
    '''
    ecd=""                             
    for i in msg:
        if(i.islower()):
            ecd += chr((ord(i)+k) % (26+97))    #converting character to ascii value then performing (P+K) mod 26 to encode the msg.
        elif(i.isupper()):
            ecd += chr((ord(i)+k) % (26+65))
        else:
            ecd += i

    return ecd

    

def decode(msg,k):
    '''
    Purpose:- This function is desined to decode the given message.
    Input:-   msg:takes string value as an input.
    Output:-  Returns decoded message.
    e.g.:-
            I/P: msg = CDEF 123 , k = 2
            O/P: ABCD 123
    '''
    dcd=""                                 
    for i in msg:
        if(i.islower()):
            dcd += chr((ord(i)-k) % (26+97))    #converting character to ascii value then performing (P-K) mod 26 to decode the msg.
        elif(i.isupper()):
            dcd += chr((ord(i)-k) % (26+65))
        else:
            dcd += i
        
    return dcd                              



def main():
    '''
    Driver code
    '''
    msg=input("Enter the message to encode : ")          
    k = int(input("Enter the number: "))
    en=encode(msg,k)                                       
    print("The message you entered:",msg)                
    print("The message after encoding :",en)             
    print("The message after decoding it :",decode(en,k))  
    
if __name__=='__main__':
    main()      #calling main() function. 