'''
Write a program that can perform a letter frequency attack on any monoalphabetic substitution cipher without
human intervention. Your software should produce possible plain text in rough order of likelihood. It would be
good if your user interface allows user to specify " Give me top 10 possible plain texts"
'''

"""
Purpose :   Function to decrypt monoalphabetic substitution cipher using the letter frequency attack
Input   :   encrypted_msg -> encrypted text which we want to decrypt
            no_of_outcome -> total number of top possible plain texts we want
Ouput   :   a list contain all possbile plain text
"""
def frequencyattaack(encrypted_msg, no_of_outcome):
    # lower aphabate i.e abcdefghijklmnopqrstuvwxyz (Default)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # It will Store the frequency of each letter in encrypted text
    freq = [0] * len(alphabet)

    # Stores the frequency of each letter in encrypted text in descending order
    freq_sorted = [0]*len(alphabet)

    # Store which alphabet is used already
    used_alphabet = [0] * len(alphabet)

    #  Stores all final possible deciphered plaintext
    plain_text = list()

    # Traverse encrypted text
    # and find frequency of each chiper text
    # whitespace, symbol and digit are not included
    for char in encrypted_msg:
        if char in alphabet:
            freq[alphabet.index(char)] += 1
            freq_sorted[alphabet.index(char)] += 1

    # Sort the frequency in descending order
    freq_sorted.sort(reverse=True)

    # letter frequenty used in english language
    frequenty_used = "etaoinshrdlcumwfgypbvkjxqz"

    # Itearate for all possible outcome
    for i in range(no_of_outcome):
        ch = -1

        # Iterate over the range [0, 26]
        for j in range(26):
            if freq_sorted[i] == freq[j] and used_alphabet[j] == 0:
                used_alphabet[j] = 1
                ch = j
                break

        if ch == -1:
            break

        # Store the numerical equivalent of letter
        # at ith index of array letter_frequency
        x = ord(frequenty_used[i]) - 65

        # Calculate the probable shift used
        # in monoalphabetic cipher
        x = x - ch

        # Temporary string to generate one
        # plaintext at a time
        curr = ""

        # Generate the probable ith plaintext
        # string using the shift calculated above
        for k in range(len(encrypted_msg)):

            # Insert whitespaces as it is
            if encrypted_msg[k] == ' ':
                curr += " "
                continue

            # here Shifting the kth letter of the
            # cipher by x 
            y = ord(encrypted_msg[k]) - 65
            y += x

            if y < 0:
                y += 26
            if y > 25:
                y -= 26

            # here Additon of the kth calculated/shifted
            # here letter to temporary string
            curr += chr(y + 65)

        plain_text.append(curr)

    return plain_text


# It is a main function from where execution is done
if __name__ == "__main__":
# Here Encrypted msg it taken from the user
    encrypted_msg = input("Enter the encrypted message:\n").upper()
    while(True):
        try:
            no_of_possible_ouput = int(
                input("\nEnter the number of possible text "))
            break
        except:
            print("Enter correct number of possible text")

    print("\n So Possible Plan text are : \n")
    plain_txt =frequencyattaack(encrypted_msg, no_of_possible_ouput)

    for txt in plain_txt:
        print(txt+"\n\n")
        
    print("\n Thank you")
