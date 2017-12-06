def create_Dictionaries():
    course_Room = {}
    course_Room['CS101'] = '3004'
    course_Room['CS102'] = '4501'
    course_Room['CS103'] = '6755'
    course_Room['NT110'] = '1244'
    course_Room['CM241'] = '1411'
    
    course_Instructor = {
    course_Instructor['CS101'] = 'Haynes'
    course_Instructor['CS102'] = 'Alvarado'
    course_Instructor['CS103'] = 'Rich'
    course_Instructor['NT110'] = 'Burke'
    course_Instructor['CM241'] = 'Lee'

    course_Time = {}
    course_Time['CS101'] = '8:00 a.m.'
    course_Time['CS102'] = '9:00 a.m.'
    course_Time['CS103'] = '10:00 a.m.'
    course_Time['NT110'] = '11:00 a.m.'
    course_Time['CM241'] = '1:00 p.m.'

    return course_Room, course_Instructor, course_Time

def get_Course_Number(course_Room, course_Instructor, course_Time):
    course_Number = input('Enter a course number: ')
    room = course_Room[course_Number]
    instructor = course_Instructor[course_Number]
    time = course_Time[course_Number]

    print( "The details for course", course_Number, " are:")
    print("Room:", room, "\nInstructor:", instructor, "\nTime:", time, sep=' ')

def main ():
    course_Room, course_Instructor, course_Time = create_Dictionaries()
    get_Course_Number(course_Room, course_Instructor, course_Time)
    
main()
