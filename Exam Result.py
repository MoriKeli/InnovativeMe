print('Program written by: Mori Keli\nAll Rights Reserved.\nNo part of this code can be copied, changed or altered'
      ' without my Permission.\nFailure to comply with this simple terms itafanya tukosane!!\n VIBAYA SANA!!!!')

# Write a program that processes examination results of a certain school.
# The program accepts user's input which is Student Name, Index Number and the number of subjects the student is taking.
# The program should process details of 3 students.

for i in range(3):
    stud_name = input('Enter your name: ')
    index = int(input('Enter your index number: '))
    sub = int(input('enter the number of subjects you are taking: '))

    """" The program does not accept the user's input about the student's score in each subject if the number of 
         subjects is not equal to 11. """

    if sub != 11:
        print('Invalid Entry!!! A Student is required to take a minimum of 11 subjects.')
        continue
    else:
        print(stud_name, index, 'is taking', sub, 'subjects.')

# The program allows the user to enter student's score in each subject for each student.
    """ Score per subject is between 0 and 100. The program displays an error message if the score is not 
        within this range,and does not process the student's examination result """

    mat = int(input('What did this student score in Mathematics? '))
    if mat <0 or mat >100:
        print('This score is out of range. Please try again.')
        continue
    eng = int(input('What did this student score in English? '))
    if eng <0 or eng >100:
        print('This score is out of range. Please try again!!')
        continue
    kis = int(input('What did this student score in Kiswahili? '))
    if kis <0 or kis >100:
        print('This score is out of range. Please try again!!')
        continue
    chem = int(input('What did this student score in Chemistry? '))
    if chem <0 or chem >100:
        print('This score is out of range. Please try again!!')
        continue
    bio = int(input('Wht did this student score in Biology? '))
    if bio <0 or bio >100:
        print('This score is out of range. Please try again!!')
        continue
    phy = int(input('What this student score in Physics? '))
    if phy <0 or phy >100:
        print('This score is out of range. Please try again!!')
        continue
    hist = int(input('What is the student''s score in History? '))
    if hist <0 or hist >100:
        print('This score is out of range. Please try again!!')
        continue
    geo = int(input('What did this student score in Geography? '))
    if geo <0 or geo >100:
        print('This score is out of range. Please try again!!')
        continue
    cre = int(input('What did this student score in CRE? '))
    if cre <0 or cre >100:
        print('This score is out of range. Please try again!!')
        continue
    biz = int(input('What did this student score in Business Studies? '))
    if biz <0 or biz > 100:
        print('This score is out of range. Please try again.')
        continue
    comp = int(input('What did this student score in Computer Studies? '))
    if comp <0 or comp >100:
        print('This score is out of range. Please try again!!')
        continue

# The program calculates the average score of each student.

    average = (mat+eng+kis+chem+bio+phy+hist+geo+cre+biz+comp)/11

# The program assigns grades to each student based on their average and displays the grade each student has scored.

    if average >= 80 and average <= 100:
        print(i, stud_name, index, 'Scored an A.')
    if average >= 60 and average < 80:
        print(i, stud_name, index, 'scored a B.')
    if average >= 40 and average < 60:
        print(i, stud_name, index, 'scored C.')
    if average >= 20 and average < 40:
        print(i, stud_name, index, 'scored a D.')
    if average < 20:
        print(i, stud_name, index, 'scored an E.')
