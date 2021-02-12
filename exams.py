""" Program written by: Mori Keli.
    All Rights Reserved. No part of this code may be copied, changed or altered without my Permission.
    Failure to comply with this simple terms itafanya tukosane!!! VIBAYA SANA!!!! """
# Write a program that calculates the examination results of a single student.

for i in range(1):

    # The program accepts student name, index number and number of subjects the student is studying.
    # Student name is first name and last name.
    f_name = input('Enter the student\'s first name: ')
    l_name = input('Enter your student\'s last name: ')
    stud_name = f_name+l_name

    # The program displays an error message if the student name contains spaces, numbers or special characters.
    if stud_name.isalpha():
        """ The program allows the user to enter name of secondary school and the index number 
            if the student name is correct."""
        sec = input('Enter the name of your secondary school: ')
        index = int(input('Enter this student index number: '))
    else:
        print('INVALID NAME!! Please check the correct spelling of this Student Name.')
        break   # The program is terminated if the Student Name contains numbers or special characters.

    # The program displays an error message if the students enters the number of subjects less than or exceeding 11.
    subj = int(input('How many subjects are you taking? '))
    if subj!=11:
        print('INVALID DATA!!! A student is allowed to take 11 subjects. Please try again.')
    else:   # If the number of subjects is 11, the program allows the user to enter scores in each subject.
        mat = int(input('Enter your score in Mathematics: '))
        # The score of each subject ranges from 0-100.
        if mat<0 or mat>100:
            """ An error message is displayed if the  range is not 0 or 100. """
            print('ERROR!! this score is out of range. Please try again.')
            break   # The program is terminated if the range is less than 0 or greater than 100.
        # If the score for each subjects lies within the range, your score will be displayed in the next statement.
        else:
            print('Your score in Mathematics is: ', mat)
        eng = int(input('Enter your score in English: '))
        if eng<0 or eng>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in English is: ', eng)
        kisw = int(input('Enter your score in Kiswahili: '))
        if kisw<0 or kisw>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in Kiswahili is: ', kisw)
        chem = int(input('Enter your score in Chemistry: '))
        if chem<0 or chem>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in Chemistry is: ', chem)
        bio = int(input('Enter your score in Biology: '))
        if bio<0 or bio>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in Biology is: ', bio)
        phy = int(input('Enter your score in Physics: '))
        if phy<0 or phy>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in Physics is: ', phy)
        hist = int(input('Enter your score in History: '))
        if hist<0 or hist>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in History is: ', hist)
        geo = int(input('Enter your score in Geography: '))
        if geo<0 or geo>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in Geography is: ', geo)
        cre = int(input('Enter your in CRE: '))
        if cre<0 or cre>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in CRE is: ', cre)
        comp = int(input('Enter your score in Computer Studies: '))
        if comp<0 or comp>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score in Computer Studies is: ', comp)
        bis = int(input('Enter your score in Business Studies: '))
        if bis<0 or bis>100:
            print('ERROR!! this score is out of range. Please try again.')
            break
        else:
            print('Your score is Business Studies is: ', bis)

        # This next program single-dashed line to separate the output from the input. The line is 28 dashes long.
        print('---'*29)
        print('---'*9, sec.upper(), '---'*10)
        print('---'*9, 'MOTTO: Sky is the limit', '---'*11)
        # To calculate total score, the variable total will do the math.
        total = (mat+eng+kisw+chem+bio+phy+hist+geo+cre+comp+bis)

        # To calculate the average of the student, the variable avg will do the math.
        avg = total/11   # To get average, the program divides total by 11 subjects.

        """ If the average is greater than or equal to 80 and less than or equal to 100, the program will display 
            student name, index number, score per subject, total, average and assign the student grade D. """
        if avg>=80 and avg<=100:
            print('Student Name: ',  f_name+' '+l_name, '\nIndex Number: ', index,  '\nNo. of Subjects: ', subj)

            # The program print a line 15 dashes long below Student name, Index Number and the number of subjects.
            print('---'*29)     # The line separates student details from scores per subject.
            print('\nMathematics: ', mat, '\nEnglish: ', eng, '\nKiswahili: ', kisw, '\nChemistry: ', chem,
                  '\nBiology: ', bio, '\nPhysics: ', phy, '\nHistory: ', hist, '\nGeography: ', geo,
                  '\nCRE: ', cre, '\nComputer Studies: ', comp, '\nBusiness Studies: ', bis, '\nTotal: ', total)
            print('Average: ', round(avg, 2))     # The program displays the average.
            print('Grade: A')   # The program assigns the grade depending on the average. In this case grade A.
            print('---'*25)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment:  Excellent Performance. A Bright student. Keep it up!')

            """ If the average is greater than or equal to 60 and less than 80, the program will display student name,
             index number, score per subject, total, average and assign the student grade B. """
        elif avg>=60:
            print('Student Name: ', f_name+' '+l_name, '\nIndex Number: ', index, '\nNo. of Subjects: ', subj)
            print('---'*29)      # The line separates student details from scores per subject.
            print('\nMathematics: ', mat, '\nEnglish: ', eng, '\nKiswahili: ', kisw, '\nChemistry: ', chem,
                  '\nBiology: ', bio, '\nPhysics: ', phy, '\nHistory: ', hist, '\nGeography: ', geo,
                  '\nCRE: ', cre, '\nComputer Studies: ', comp, '\nBusiness Studies: ', bis, '\nTotal: ', total)
            print('Average: ', round(avg, 2))     # The program displays the average.
            print('Grade: B')   # The program assigns the grade depending on the average. In this case grade B.
            print('---'*25)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: Above average. Good Work. Keep it up!!')

            """ If the average is greater than or equal to 40 and less than 60, the program will display student name, 
                index number, score per subject, total, average and assign the student grade C. """
        elif avg>=40:
            print('Student Name: ', f_name+' '+l_name, '\nIndex Number: ', index, '\nNo. of Subjects: ', subj)
            print('---'*29)     # The line separates student details from scores per subject.
            print('\nMathematics: ', mat, '\nEnglish: ', eng, '\nKiswahili: ', kisw, '\nChemistry: ', chem,
                  '\nBiology: ', bio, '\nPhysics: ', phy, '\nHistory: ', hist, '\nGeography: ', geo,
                  '\nCRE: ', cre, '\nComputer Studies: ', comp, '\nBusiness Studies: ',  bis, '\nTotal: ', total)
            print('Average: ', round(avg, 2))    # The program displays the average.
            print('Grade: C')   # The program assigns the grade depending on the average. In this case grade C.
            print('---'*25)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: An Average Student. Improve.')

            """ If the average is greater than or equal to 20, the program will display student name, index number, 
                score per subject, total, average and assign the student grade D. """
        elif avg>=20:
            print('Student Name: ', f_name+' '+l_name, '\nIndex Number: ', index, '\nNo. of Subjects: ', subj)
            print('---'*29)     # The line separates student details from scores per subject.
            print('\nMathematics: ', mat, '\nEnglish: ', eng, '\nKiswahili: ', kisw, '\nChemistry: ', chem,
                  '\nBiology: ', bio, '\nPhysics: ', phy, '\nHistory: ', hist, '\nGeography: ', geo,
                  '\nCRE: ', cre, '\nComputer Studies: ', comp, '\nBusiness Studies: ',  bis, '\nTotal: ', total)
            print('Average: ', round(avg, 2))     # The program displays the average.
            print('Grade: D')   # The program assigns a grade depending on the average. In this case grade D.
            print('---'*25)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: Below Average. Work Hard.')

            """ If the average is less than 20, the program will display student name, index number, score per 
                         subject, total, average and assign the student grade E. """
        else:
            print('Student Name: ', f_name+' '+l_name, '\nIndex Number: ', index, '\nNo. of Subjects: ', subj)
            print('---'*29)     # The line separates student details from scores per subject.
            print('\nMathematics: ', mat, '\nEnglish: ', eng, '\nKiswahili: ', kisw, '\nChemistry: ', chem,
                  '\nBiology: ', bio, '\nPhysics: ', phy, '\nHistory: ', hist, '\nGeography: ', geo,
                  '\nCRE: ', cre, '\nComputer Studies: ', comp, '\nBusiness Studies: ',  bis, '\nTotal: ', total)
            print('Average: ', round(avg, 2))     # The program displays the average.
            print('Grade: E')   # The program assigns a grade depending on the average. In this case grade E.
            print('---'*25)     # This line encloses teacher's comment based on the student's performance.
            print('Class Teacher Comment: Poor Performance. Read your Books thoroughly.')

    # The program prints double-dashed line to signify end of loop. The lines are 29 dashes long.
    print('---'*29)
    print('---'*29)

    # The program prints the student name and index number after the two dashed lines.
    print('[Student Name: ', f_name+' '+l_name, ']\t|\t[', 'Index Number: ', index, ']')
k = input('Press ENTER to exit')
