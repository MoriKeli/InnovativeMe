# Write a program that calculates the results of CAT 1, CAT 2 & MAIN EXAMS of a comrade.
# This program uses a command line interface.
# The program prints a command-lined welcome screen.
print('***'*30)
print('***'*30)
print('\t'*4, '***WELCOME SCREEN***')
print('\t'*3, 'CAMPUS EXAMINATION RESULTS')
print('\t'*3, 'Programmer: --MORI KELI--')

# To enter student details the user has to press space bar once and press ENTER key.
space = input('Press SPACE BAR once and ENTER to continue: ')
print('***'*30)
print('***'*30)

if space == ' ':    # This line creates space as a string.
    num = int(input('Enter the number of student(s): '))    # The user enters how many students are involved.
    if num<1:   # No. of students should not be less than 1.
        print('***'*25)
        print('\t'*7, 'ERROR!!!')
        print('\tThe minimum number of students required is 1. Please try again.')
        print('***'*25)
    for i in range(num):    # The program loops according to the number of students entered.
        stud_name = input('Enter your name: ')  # The program asks for student name.
        if stud_name.isascii():
            # If stud_name is ascii, the program allows the student to enter the name of their university.
            cam = input('Enter the name of your university: ')  # The program asks for campus name.
            if cam.isascii():
                # If the campus name is ascii, the program allows the user to enter their registration number
                # in that university.

                # The program asks the user to enter their registration number in their respective university.
                reg = input('Enter your Registration Number: ')

                if reg.isalnum():
                    # The program asks the user to enter the course they are studying in their respective university.
                    co_se = input('Enter the name of the course you are studying: ')
                    # The system stores a list of courses recognized by the program.
                    # The list is used to detect if the user input corresponds with this list else
                    # the program prints out an error message.
                    C = ['Computer science', 'Computer Science', 'computer science', 'COMPUTER SCIENCE', 'BIOCHEMISTRY',
                         'b                            iochemistry',
                         'Biochemistry', 'BioChemistry']

                    # This line print an error if the course entered has the wrong spellings.
                    if co_se != C:
                        print('***' * 25)
                        print('\t' * 6, 'INVALID DATA!!!')
                        print('\t' * 4, 'THE COURSE YOU ENTERED IS INVALID.')
                        print('\t' * 3, 'The spelling of the course you entered is wrong.')
                        print('***' * 25)
                        break    # The program is terminated if the course entered has wrong spellings.

                    # The program stores a list of courses not recognized by this program.
                    L = ['Fashion and Design', 'Zoology', 'Botany', 'Chemistry', 'Physics',
                         'Bachelor of Education', 'Agricultural Science', 'Mathematics', 'FASHION & DESIGN', 'zoology',
                         'BOTANY', 'CHEMISTRY', 'PHYSICS', 'BACHELOR OF EDUCATION', 'Fashion & design'
                         'fashion & design', 'MATHEMATICS', 'AGRICULTURAL SCIENCE']
                    if co_se == L:  # The program prints an error message if the course entered is in list L.
                        print('***'*30)
                        print('\t'*3, 'COMPUTER SCIENCE IS THE ONLY RECOGNISED COURSE IN THIS PROGRAM')
                        print('\t'*2, 'THIS SITE IS STILL UNDER CONSTRUCTION. SORRY FOR THE INCONVENIENCES CAUSED.')
                        print('***'*30)
                        break   # The program is terminated if course entered is in list L.
                    elif co_se.isascii():

                        # The program asks the user to enter which study programme they are taking in their respective
                        # courses.
                        pro = input('Enter your programme e.g.(\'Certificate\', \'Diploma\', \'Degree\'): ')
                        if pro == 'Degree' or pro.isupper() or pro.islower():
                            # A degree comprises of Bachelor of Science(Bsc.), Bachelor of Arts(BA) and
                            # Bachelor of Education(B.ed)
                            bach = input(str('For Bachelor of Science, enter \'1\', for Bachelor of Arts, enter \'2\''
                                             ' else \'3\': '))
                            # If the user enters '1' the program allows the user to enter their year of study
                            # and semester.
                            if bach == '1':
                                yr = int(input('Enter Year of Study: '))
                                if yr<1 or yr>12:
                                    print('***'*25)
                                    print('\t'*6, 'ERROR!!!', '\nThe minimum year required is 1 while the maximum is '
                                                              '12. Please try again.')
                                    print('***'*25)
                                    break
                                else:
                                    sem = int(input('Enter Semester: '))
                                    if sem<1 or sem>2:
                                        print('***'*25)
                                        print('\t'*6, 'ERROR!!!', '\nThere are only two semesters in one academic yr.')
                                        print('***'*25)
                                        break
                            # If the user enters '2' or '3', the program alerts the user that
                            # the program under this category is still under construction.
                            elif bach == '2' and co_se!=L:
                                print('---'*25)
                                print('---'*25)
                                print('\t'*5, '**BACHELOR OF ARTS/BACHELOR OF EDUCATION**')
                                print('\t'*6, 'Program currently under construction')
                                break    # The program is terminated if the user enters '1' or '2'.

                    # If the user enters computers science as his/her course, then all units under computer science
                    # are displayed.
                    if co_se=='Computer Science' or co_se=='computer science' or co_se=='COMPUTER SCIENCE':
                        mat = int(input('Enter your score in MAT 110 CAT 1: '))
                        # The score for each unit in CAT 1 ranges from 0-30.
                        # The program displays an error message and is terminated if the score entered is out of range.
                        if mat<0 or mat>30:
                            print('***'*20)
                            print('\t'*4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***'*20)
                            break   # The program is terminated if the score entered is out of range.
                        phy = int(input('Enter your score in PHY 110 CAT 1: '))
                        if phy<0 or phy>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        sta = int(input('Enter your score in STA 111 CAT 1: '))
                        if sta<0 or sta>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        com = int(input('Enter your score in COM 110 CAT 1: '))
                        if com<0 or com>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        cos = int(input('Enter your score in COS 100 CAT 1: '))
                        if cos<0 or cos>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        mic = int(input('Enter your score in MIC 117 CAT 1: '))
                        if mic<0 or mic>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break

                        # This line calculates the sum of all scores in CAT 1.
                        total = mat+phy+sta+com+cos+mic

                        # The program asks the user if he/she has done CAT 2. If yes, the following lines are printed.
                        cat2 = input(str('Have you done CAT 2? (yes/no): '))
                        if cat2=='yes' or cat2=='YES' or cat2=='Yes' or cat2=='y' or cat2=='Y':
                            mat2 = int(input('Enter your score in MAT 110 CAT 2: '))
                            if mat2<0 or mat>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            phy2 = int(input('Enter your score in PHY 110 CAT 2: '))
                            if phy2<0 or phy2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            sta2 = int(input('Enter your score in STA 111 CAT 2: '))
                            if sta2<0 or sta2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            com2 = int(input('Enter your score in COM 110 CAT 2: '))
                            if com2<0 or com2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            cos2 = int(input('Enter your score in COS 100 CAT 2: '))
                            if cos2<0 or cos2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            mic2 = int(input('Enter your score in MIC 117 CAT 2: '))
                            if mic2<0 or mic2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break

                            # This line calculates the sum of all scores in CAT 2.
                            total2 = mat2+phy2+sta2+com2+cos2+mic2

                            # The program asks the user if s/he has done main exams, if yes, the program allows the user
                            # to enter their score in MAIN EXAMS.
                            main = input('Have you done main exams? (yes/no): ')
                            # if yes, the program allows the user to enter their score in each unit in MAIN EXAMS.
                            if main=='YES' or main=='Yes' or main=='yes' or main=='y' or main=='Y':
                                mat3 = int(input('Enter your score in MAT 110 MAIN EXAM: '))
                                if mat3<0 or mat>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                phy3 = int(input('Enter your score in PHY 110 MAIN EXAM: '))
                                if phy3<0 or phy3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                sta3 = int(input('Enter your score in STA 111 MAIN EXAM: '))
                                if sta<0 or sta>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                com3 = int(input('Enter your score in COM 110 MAIN EXAM: '))
                                if com3<0 or com>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                cos3 = int(input('Enter your score in COS 100 MAIN EXAM: '))
                                if cos3<0 or cos3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                mic3 = int(input('Enter your score in MIC 117 MAIN EXAM: '))
                                if mic3<0 or mic3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break

                                # The line calculates the sum of all scores in MAIN EXAMS.
                                total3 = mat3+phy3+sta3+com3+cos3+mic3
                                # This line calculates average of sum of scores in CAT 1&2, and MAIN EXAMS.
                                avg = (total+total2)/2+total3
                                # This line prints the exam report card of each student.
                                print('==='*30)
                                # The report card contains Student Details such as Name, Campus, Registration Number,
                                # Programme and Course.
                                print('Student Name\t: ', stud_name, '\nCampus\t\t: ', cam,
                                      '\nRegistration Number : ', reg)
                                print('==='*30)
                                print('==='*30)

                                # This line prints units, scores in each unit, CAT 1&2, and MAIN EXAMS.
                                print('UNIT', '\t\t\tCAT 1', '\t\t\tCAT 2', '\t\t\tMAIN EXAM')
                                print('==='*30)
                                print('MAT 110: ', '\t\t', mat, '\t\t\t', mat2, '\t\t\t\t', mat3)
                                print('PHY 110: ', '\t\t', phy, '\t\t\t', phy2, '\t\t\t\t', phy3)
                                print('STA 111: ', '\t\t', sta, '\t\t\t', sta2, '\t\t\t\t', sta3)
                                print('COM 110: ', '\t\t', com, '\t\t\t', com2, '\t\t\t\t', com3)
                                print('COS 100: ', '\t\t', cos, '\t\t\t', cos2, '\t\t\t\t', cos3)
                                print('MIC 117: ', '\t\t', mic, '\t\t\t', mic2, '\t\t\t\t', mic3)
                                print('==='*30)
                                print('==='*30)

                                # If the average is >=70 and <=100, the program prints the average of each student.
                                if avg>= 70 or avg<=100:
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: A', '\t\tPERFORMANCE: EXCELLENT')
                                elif avg>=60:   # The program prints the an average that ranges from 60-69.
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: B', '\t\tPERFORMANCE: GOOD.')
                                elif avg>=50:   # The program prints an average that ranges from 50-59.
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: C', '\t\tPERFORMANCE: AVERAGE.')
                                elif avg>=40:   # Th program prints an average that ranges from 40-49.
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: D', '\t\tPERFORMANCE: PASS.')
                                else:   # The program print an average that is below 40.
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: E', '\t\tPERFORMANCE: FAIL.')
                                # Besides average, the program displays performance of the student based on his average.

                            # The program prints out a warning if the user if the did not do the MAIN EXAMS.
                            # The program will print scores in CAT 1 & 2 if the user did not do the MAIN EXAM.
                            else:
                                print('***'*25)
                                print('\t'*6, 'WARNING!!!')
                                print('\t'*2, stud_name, reg, 'did not attempt MAIN EXAMS')
                                print('---'*25)
                                print('***'*25)

                    # If the course entered is BioChemistry, the program allows the user to enter scores in each unit
                    # attached to that course.
                    elif co_se=='BioChemistry' or co_se=='biochemistry' or co_se=='BIOCHEMISTRY':
                        mat = int(input('Enter your score in MAT 110 CAT 1: '))
                        if mat<0 or mat>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        che = int(input('Enter your score in CHE 110 CAT 1: '))
                        if che<0 or che>100:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        bot = int(input('Enter your score in BOT 110 CAT 1: '))
                        if bot<0 or bot>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        zoo = int(input('Enter your score in ZOO 110: '))
                        if bot<0 or bot>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        com = int(input('Enter your score in COM 110 CAT 1: '))
                        if com<0 or com>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break

                        sta = int(input('Enter your score in STA 111 CAT 1: '))
                        if sta<0 or sta>30:
                            print('***' * 20)
                            print('\t' * 4, 'ERROR!!!')
                            print('\tThis score is out of range. Please try again.')
                            print('***' * 20)
                            break
                        total = mat+che+bot+zoo+com+sta

                        cat2 = input('Have you done CAT 2: (yes/no): ')
                        if cat2=='yes' or cat2=='YES' or cat2=='Yes':
                            mat2 = int(input('Enter your score in MAT 110 CAT 2: '))
                            if mat2<0 or mat2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            che2 = int(input('Enter your score in CHE 110 CAT 2: '))
                            if che2<0 or che2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            bot2 = int(input('Enter your score in BOT 110 CAT 2: '))
                            if bot2<0 or bot>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            zoo2 = int(input('Enter your score in ZOO 100 CAT 2: '))
                            if zoo2<0 or zoo2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            com2 = int(input('Enter your score in COM 110 CAT 2: '))
                            if com2<0 or com2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break
                            sta2 = int(input('Enter your score in STA 111: '))
                            if sta2<0 or sta2>30:
                                print('***' * 20)
                                print('\t' * 4, 'ERROR!!!')
                                print('\tThis score is out of range. Please try again.')
                                print('***' * 20)
                                break

                            print('==='*20)
                            print('\t'*7, 'MAIN EXAM')
                            print('==='*20)

                            total2 = mat2+che2+bot2+zoo2+com2+sta2

                            main = input('Have you done MAIN EXAM? (yes/no):')
                            if main=='Yes' or main=='yes' or main=='Yes':
                                mat3 = int(input('Enter your score in MAT 110 MAIN EXAMS: '))
                                if mat3<0 or mat>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                che3 = int(input('Enter your score in CHE 110 MAIN EXAMS: '))
                                if che3<0 or che3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                bot3 = int(input('Enter your score in BOT 110 MAIN EXAMS: '))
                                if bot3<0 or bot3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                zoo3 = int(input('Enter your score in ZOO 110 MAIN EXAMS: '))
                                if zoo3<0 or zoo3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                com3 = int(input('Enter your score in COM 110 MAIN EXAMS: '))
                                if com3<0 or com>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break
                                sta3 = int(input('Enter your score in STA 111 MAIN EXAMS: '))
                                if sta3<0 or sta3>100:
                                    print('***' * 20)
                                    print('\t' * 4, 'ERROR!!!')
                                    print('\tThis score is out of range. Please try again.')
                                    print('***' * 20)
                                    break

                                total3 = mat3+che3+bot3+zoo3+com3+sta3
                                avg = (total+total2)/2+total3
                                print('===' * 30)
                                print('Student Name\t: ', stud_name, '\nCampus\t\t: ', cam,
                                      '\nRegistration Number : ', reg)
                                print('===' * 30)
                                print('===' * 30)
                                print('UNIT', '\t\t\tCAT 1', '\t\t\tCAT 2', '\t\t\tMAIN EXAM')
                                print('===' * 30)
                                print('MAT 110: ', '\t\t', mat, '\t\t\t', mat2, '\t\t\t\t', mat3)
                                print('CHE 110: ', '\t\t', che, '\t\t\t', che2, '\t\t\t\t', che3)
                                print('STA 111: ', '\t\t', sta, '\t\t\t', sta2, '\t\t\t\t', sta3)
                                print('COM 110: ', '\t\t', com, '\t\t\t', com2, '\t\t\t\t', com3)
                                print('ZOO 110: ', '\t\t', zoo, '\t\t\t', zoo2, '\t\t\t\t', zoo3)
                                print('STA 111: ', '\t\t', sta, '\t\t\t', sta2, '\t\t\t\t', sta3)
                                print('===' * 30)
                                print('===' * 30)
                                if avg >= 70 or avg <= 100:
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: A', '\t\tPERFORMANCE: EXCELLENT')
                                elif avg >= 60:
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: B', '\t\tPERFORMANCE: GOOD.')
                                elif avg >= 50:
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: C', '\t\tPERFORMANCE: AVERAGE.')
                                elif avg >= 40:
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: D', '\t\tPERFORMANCE: PASS.')
                                else:
                                    print('AVERAGE: ', avg, '\t\t\tGRADE: E', '\t\tPERFORMANCE: FAIL.')

else:
    print('==='*30)
    print('\t'*7, '!!!PROGRAM UNREACHABLE!!!')
    print('==='*30)

etp = input('Press ENTER to Exit.')
