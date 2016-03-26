def my_final_grade_calculation(filename):
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    lines = file_pointer.readlines()
    out_list = {}
    for line in lines:
        line = line.strip('\n')
        line = line.replace(',', '')
        words = line.split()
        name = words[0]
        q1 = int(words[1])
        q2 = int(words[2])
        q3 = int(words[3])
        q4 = int(words[4])
        q5 = int(words[5])
        q6 = int(words[6])
        a1 = int(words[7])
        a2 = int(words[8])
        a3 = int(words[9])
        a4 = int(words[10])
        midterm = int(words[11])
        final = int(words[12])

        quizzes = sorted([q1, q2, q3, q4, q5, q6], reverse=True)
        assignments = sorted([a1, a2, a3, a4], reverse=True)

        score_quizzes = (float(quizzes[0] + quizzes[1] + quizzes[2] + quizzes[3]) / 4) * 0.25
        score_assignments = (float(assignments[0] + assignments[1] + assignments[2]) / 3) * 0.25
        score_midterm = float(midterm) * 0.25
        score_final = float(final) * 0.25
        
        #print(score_quizzes, score_assignments, score_midterm, score_final)
        total_score = score_quizzes + score_assignments + score_midterm + score_final
        passfail = 'fail'
        if (total_score >= 60):
            passfail = 'pass'
            
        out_list[name] = passfail
        
    return out_list

print(my_final_grade_calculation('C:\\Temp\\test.txt'))
