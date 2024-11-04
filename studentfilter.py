
def select_students(students, threshold):

    output = {'Accepted': [], 'Rejected': []}

    for student_score in students:

        if student_score[1] >= threshold:
            output['Accepted'].append(student_score)
        else:
            output['Rejected'].append(student_score)

    output1 = {'Accepted': sorted(output['Accepted'], key=lambda x: x[1], reverse=False), 'Rejected': sorted(output['Rejected'], key=lambda x: x[1], reverse=True)}

    return output1


def select_student(students, threshold):
    accepted = []
    rejected = []

    for student_score in students:
        if student_score[1] >= threshold:
            accepted.append(student_score)
            accepted.sort(reverse=True, key=lambda s: s[1])
        else:
            rejected.append(student_score)
            rejected.sort(reverse=False, key=lambda s: s[1])

    output = {'Accepted': accepted, 'Rejected': rejected}

    return output


if __name__ == "__main__":
    my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 22], ['Ben Ball', 54], ['William Lee', 2], ['Henry Lee', 15]]
    print(select_student(my_class, 20))
