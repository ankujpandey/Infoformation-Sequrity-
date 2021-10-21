#This program is designed to encode and decode the mesasage using 2*2 Hill cipher:
def get_keyMatrix(key):
    '''
    Purpose:- This function is desined to make matrix of given strings.
    Input:-   key:takes string value as an input.
    Output:-  Returns matrix of index value of each character.
    e.g.:-
            I/P: msg = HILL
            O/P: |7    8|
                 |11  11|
    '''
    k = 0
    keyMatrix = [[0]*2 for x in range(2)]
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[k]) - 65
            k+=1
    return keyMatrix

def get_msgVector(msg):
    '''
    Purpose:- This function is desined to divide the string into parts of 2 characters.
    Input:-   msg:takes string value as an input.
    Output:-  Returns 2 dimentional list of characters of given string.
    e.g.:-
            I/P: msg = HELLO
            O/P: [['H','E'],['L','L']['O','']]
    '''
    return [[msg[i+j:i+j+1] for j in range(2)] for i in range(0, len(msg),2)]

def formula(mat1,mat2):
    '''
    Purpose:- This function is desined to apply the formula for encoding the characters.
    Input:-   mat1:takes list as an input.
              mat2: takes 2 dimentional list as an input.
    Output:-  Returns list of ASCII value of Characters of string.
    e.g.:-
            I/P: mat1 = |0  1|  mat2 = |7   8|
                                       |11 11|
            O/P: |77  77|
    '''
    cipher_mat = [0]*2
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            cipher_mat[i] += (ord(mat1[j])-65) * mat2[j][i]
        cipher_mat[i] = (cipher_mat[i] % 26) + 65
    return cipher_mat

def determinant(keyMat):
    '''
    Purpose:- This function is desined to find the determinant of given matrix.
    Input:-   keyMat:takes matrix as an input.
    Output:-  Returns the determinant.
    e.g.:-
            I/P:   mat2 = |7   8|
                          |11 11|
            O/P: -11
    '''
    return (keyMat[0][0]*keyMat[1][1]) - (keyMat[0][1]*keyMat[1][0])

def mod_inverse(a,b):    
    '''
    Purpose:- This function is desined to find if gcd of a mod b is 1 or not.
    Input:-   a:takes int as an input.
              b:takes int as an input.
    Output:-  Returns that number for which a mod b is 1.
    e.g.:-
            I/P: a=3 , b=26 
            O/P: 9
    '''                      
    for i in range(1,b):
        flag = (a*i) % b
        if flag == 1:
            return i
    return None

def inverseMat(keyMat,determinant):
    '''
    Purpose:- This function is desined to find the inverse of the given matrix.
    Input:-   keyMat:takes matrix as an input.
              determinant: takes int as an input.
    Output:-  Returns inverse matrix of the given matrix.
    e.g.:-
            I/P:  mat2 = |7   8|
                         |11 11|
            O/P:  |25  22|
                  |1   23|
    '''
    k_Mat = keyMat
    multiplicativeInverse = mod_inverse(determinant,26)
    k_Mat[0][0],k_Mat[1][1] = k_Mat[1][1],k_Mat[0][0]
    k_Mat[0][1] *= -1
    k_Mat[1][0] *= -1
    for i in range(2):
        for j in range(2):
            k_Mat[i][j] = (k_Mat[i][j]*multiplicativeInverse) % 26
    return k_Mat


def encode(msg,k):
    '''
    Purpose:- This function is desined to encode the given message.
    Input:-   msg:takes string value as an input.
                k:takes k(key) String value as an input.
    Output:-  Returns encoded message.
    e.g.:-
            I/P: msg = ABCD , k = HILL
            O/P: LLVX
    '''
    ecd=""          
    msgVector = get_msgVector(msg)
    k_matrix = get_keyMatrix(k)     

    for i in range(len(msgVector)):
        if(msgVector[i][1] == ''):
            msgVector[i][1] = chr(90)
            print(msgVector[i])
            chipherMat = formula(msgVector[i],k_matrix)
        else:
            chipherMat = formula(msgVector[i],k_matrix)
            ecd += chr(chipherMat[0]) + chr(chipherMat[1])

    return ecd

def decode(msg,k):
    '''
    Purpose:- This function is desined to decode the given message.
    Input:-   msg:takes string value as an input.
    Output:-  Returns decoded message.
    e.g.:-
            I/P: msg = LLVX , k = HILL
            O/P: ABCD
    '''
    dcd=""                                 
             
    msgVector = get_msgVector(msg)
    k_matrix = get_keyMatrix(k)

    det = determinant(k_matrix)
    det = det % 26     
    K_inverseMat = inverseMat(k_matrix,det)

    for i in range(len(msgVector)):
        chipherMat = formula(msgVector[i],K_inverseMat)
        dcd += chr(chipherMat[0]) + chr(chipherMat[1])

    return dcd    


def main():
    '''
    Driver code
    '''
    msg=input("Enter the message to encode : ") 
    k = input("Enter the key : ") 
    en=encode(msg,k)                                       
    print("The message you entered:",msg)                
    print("The message after encoding :",en) 
    print("the message after decodingv : ",decode(en,k))
    mat1=get_msgVector(msg)
    print(formula(mat1[0],get_keyMatrix("HILL")))
    print(inverseMat(get_keyMatrix("HILL"),15))     
    
if __name__=='__main__':
    main()      #calling main() function.