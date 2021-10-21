'''
Write a program that can perform a letter frequency attack on an additive cipher without human intervention. 
Your software should produce possible plain text in rough order of likelihood.
It would be good if your user interface allows user to specify " Give me top 10 possible plain texts"
'''
def maxFriquency(str):
    '''
    Purpose:- This function is desined to find the maximum frequency of the letters and then to throw the letter which occured most.
    Input:-   str:takes string value as an input.
    Output:-  Returns the letter wich occured most.
    e.g.:-
            I/P: str = hello
            O/P: l
    '''
    all_freq = {}
  
    #making count of each letter occured in string.
    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    
    #making list of ltters ocuured in tupple form in sorted manner by sorting values of the dict.
    list = sorted(all_freq.items(), key = lambda kv:[kv[1], kv[0]]) 

    return list[-1][0]



def decrypt(msg,maxFrequency,m):
    '''
    Purpose:- This function is desined to decode the message.
    Input:-   msg: takes string value as an input.
              maxFrequency: takes string value as an input.
              m : takes int value as an input for maximum number of outputs.
    Output:-  Returns the decoded messeges.
    e.g.:-
            I/P: msg = WKLV LV D PHVVDJH , maxFrequency = V , m = 10
            O/P:    F:;E ;E 3 ?7EE397
                    UIJT JT B NFTTBHF
                    B67A 7A / ;3AA/53
                    PDEO EO = IAOO=CA
                    J>?I ?I 7 C;II7=;
                    OCDN DN < H@NN<B@
                    THIS IS A MESSAGE
                    I=>H >H 6 B:HH6<:
                    SGHR HR @ LDRR@FD
                    E9:D :D 2 >6DD286
    '''

    alphabet_freq = "etaoinshrdlcumwfgypbvkjxqz"  #letter frequenty used in english language.

    max_freq_ascii = ord(maxFrequency.lower())
    lst = []
    for i in alphabet_freq:
        n = abs(ord(i) - max_freq_ascii)        #calculating distance between the cipher letter and alphabet letter.
        lst.append(n)
    list_decoded_msg = []
    for i in range(m):
        dcd = ''
        for j in msg:
            if(j.islower()):
                dcd += chr((ord(j)-lst[i]) % (26+97))    #converting character to ascii value then performing (P-K) mod 26 to decode the msg.
            elif(j.isupper()):
                dcd += chr((ord(j)-lst[i]) % (26+65))
            else:
                dcd += j
        
        list_decoded_msg.append(dcd)
    return list_decoded_msg


def main():
    '''
    Driver code
    '''
    msg=input("Enter the message to encode : ")
    n = int(input("Enter the number of top plain text you want to search for : "))
    max_Friquency = maxFriquency(msg)
    decoded = decrypt(msg,max_Friquency,n)
    print("The decoded msgsseges are : \n")
    for i in decoded:
        print(i)

    
    
if __name__=='__main__':
    main()      #calling main() function.
