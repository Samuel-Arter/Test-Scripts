
def select_students(students, threshold):

    output = {'Accepted': [], 'Rejected': []}

    for student_score in students:

        if student_score[1] >= threshold:
            output['Accepted'].append(student_score)
        else:
            output['Rejected'].append(student_score)

    output1 = {'Accepted': sorted(output['Accepted'], key=lambda x: x[1], reverse=False), 'Rejected': sorted(output['Rejected'], key=lambda x: x[1], reverse=True)}

    return output1

if __name__ == "__main__":
    my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 1], ['Ben Ball', 5], ['William Lee', 2]]
    print(select_students(my_class, 20))

