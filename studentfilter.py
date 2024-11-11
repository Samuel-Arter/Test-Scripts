# A script with several functions that return the same result but written in different ways

def select_students(students, threshold):
    """
    A function to determine which students have/haven't met a specific threshold

    Argument(s):
        1. (students) A list where each element is a list of a student name, and his grade.
        2. (threshold) An integer which determines whether a student will be accepted/rejected

    Returns:
        output - A dictionary containing ordered sets of lists of 'Accepted' and 'Rejected' students and their grade
    """

    output = {'Accepted': [], 'Rejected': []}

    for student_score in students:

        if student_score[1] >= threshold:
            output['Accepted'].append(student_score)
        else:
            output['Rejected'].append(student_score)

    output['Accepted'].sort(key=lambda x: x[1], reverse=True)
    output['Rejected'].sort(key=lambda x: x[1], reverse=False)

    return output


def select_student(students, threshold):
    """
    This function that returns a dictionary containing an ordered set of lists of 'accepted' and 'rejected'
    students. This function employs the use of lists unlike the last function.
    """

    accepted = []
    rejected = []

    for student_score in students:
        if student_score[1] >= threshold:
            accepted.append(student_score)
        else:
            rejected.append(student_score)

    accepted.sort(reverse=True, key=lambda s: s[1])
    rejected.sort(reverse=False, key=lambda s: s[1])

    output = {'Accepted': accepted, 'Rejected': rejected}

    return output


def student_select(students, threshold):
    """
    Returns same result as previous functions. This function employs the use of list comprehension
    """

    a = [student for student in students if student[1] >= threshold]
    r = [student for student in students if student[1] < threshold]

    result = {'Accepted': sorted(a, key=lambda s: s[1], reverse=True),
              'Rejected': sorted(r, key=lambda s: s[1])}

    return result


if __name__ == "__main__":
    my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 22], ['Ben Ball', 54], ['William Lee', 2], ['Henry Lee', 15], ['Stagger Lee', 99]]
    print(select_students(my_class, 20))
    print(select_student(my_class, 20))
    print(student_select(my_class,20))
