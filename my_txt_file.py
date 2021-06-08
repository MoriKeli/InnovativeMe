# Write a program that creates a text file and allows the users to enter any text into the file(txt file).
# The program should print the message entered by the user.
# The program should check if the file exists, if it exists it should allow the user to enter his/her message else
# create a new text file.

import os
txt_file = 'my_txt_file.txt'
if os.path.exists(txt_file):  # the system scans if the text file exists
    t_file = open('C:/Users/MORI/OneDrive/Documents/Coding/Python/my_txt_file/my_txt_file.txt', 'w')
    msg = input('Enter your message: ')  # The user enters his text.
    print('Your message: ', msg, file=t_file)   # The program displays the text entered by the user
    t_file.close()  # The file is closed after the user enters his/her text.

    # The program opens the file once again and reads the entire message entered by the user.
    msg_file = open('C:/Users/MORI/OneDrive/Documents/Coding/Python//my_txt_file/my_txt_file.txt').read()
    print(msg_file)   # Once the message is read, the program prints the txt entered by the user.

# if the file does not exist the program creates a new text file 'my_text_file'
else:
    r_file = open('C:/Users/MORI/OneDrive/Documents/Coding/Python/my_txt_file/my_txt_file.txt', 'x')
    print('This is your new text file.', file=r_file)   # This is the default message displayed.
    r_file.close()  # the file is closed after its created.

