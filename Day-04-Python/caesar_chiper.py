import string
print('''
------------------------------
!WELCOME TO THE CAESAR CHIPER!
------------------------------------------------------------------------
•this program will help you send/receive secret messages to your peers•
•encrypt & decrypt messages•
------------------------------------------------------------------------
''')
      
def endecode(message, key, status):
    space = []
    if ' ' in message:
        space = [i for i in range(len(message)) if message[i] == ' ']
        message = message.replace(' ','')
    num = [letters.index(a) for a in message]
    num = [a+key for a in num] if status == 'encode' else [a-key for a in num]
    endecoded_message = [letters[a] for a in num]
    for a in space:
        endecoded_message.insert(a, ' ')
    endecoded_message = ''.join(endecoded_message)
    return endecoded_message

letters = [a for a in string.ascii_letters]
is_continue = 1
while is_continue == 1:
    status = input("Please type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while status != 'encode' and status != 'decode':
        status = input(f"There is no program {status}.\nPlease type 'encode' to encrypt, type 'decode' to decrypt:\n")

    user_message = input("Please type your message:\n")
    shift_num = int(input("Please type the key number:\n")) % 26

    print(f"This is your {status}d message:\n{endecode(user_message, shift_num, status)}")

    is_continue = int(input("Do you want to go again? (1 for yes, 0 for no) (integer only):\n"))
