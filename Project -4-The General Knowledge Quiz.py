


import random as r
score=0
for i in range(1,6):
   
    a=r.choice(['Who created Python?','In which year was Python first released?','What keyword is used to print output in Python?',' What function is used to take user input?',' What is the extension of a Python file?', 'Is Python case-sensitive?',
    'Which data type stores text?',
    'Which data type stores whole numbers?',
    'Which data type stores decimal numbers?',
    'Which data type stores True or False?',
    'What is the output of print(5 + 3)?',
    'What is the output of print(10 // 3)?',
    'What is the output of print(10 % 3)?',
    'Which operator checks equality?',
    'Which operator means "not equal"?',
    'Which keyword is used for decision making?',
    'Which keyword is used when the first condition is false?',
    'Which keyword checks multiple conditions?',
    'Which loop repeats a fixed number of times?',
    'Which loop runs while a condition is True?',
    'Which keyword exits a loop?',
    'Which keyword skips the current iteration?',
    'Which function returns the length of a string or list?',
    'Which function converts a string to lowercase?',
    'What function converts a string to uppercase?',
    'Which function removes whitespace from both ends of a string?',
    'Which operator is used for exponentiation in Python?',
    'What is the output of print(2 ** 3)?',
    'Which function converts a string to an integer?',
    'Which function converts an integer to a string?',
    'Which function returns the type of a variable?',
    'Which keyword is used to define a function?',
    'Which keyword is used to return a value from a function?',
    'What is the default return value of a function with no return statement?',
    'Which data type is immutable: List or Tuple?',
    'Which brackets are used to create a list?',
    'Which brackets are used to create a tuple?',
    'Which brackets are used to create a dictionary?',
    'Which brackets are used to create a set?',
    'Which method adds an element to a list?',
    'Which method removes the last element from a list?',
    'Which method sorts a list?',
    'Which method reverses a list?',
    'Which function finds the maximum value in a list?',
    'Which function finds the minimum value in a list?',
    'Which function calculates the sum of a list?',
    'Which function sorts without modifying the original list?',
    'Which keyword is used to create a class?',
    'Which special method acts as a constructor in Python?'])
    print(a)
    answer=input('Enter the Answer: ')
    print(answer)
    if a=='Who created Python?' and answer=='Guido van Rossum':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score+=1
        print(f"Score: {score}")
    if a=='In which year was Python first released?' and answer=='1991':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score+=1
        print(f"Score: {score}")
    if a=='What keyword is used to print output in Python?' and answer=='print()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score+=1
        print(f"Score: {score}")
    if a==' What function is used to take user input?' and answer=='input()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score+=1
        print(f"Score: {score}")
    elif a=='Which symbol is used for comments?' and answer=='#':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score+=1
        print(f"Score: {score}")
    elif a=='What is the extension of a Python file?' and answer=='.py':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score+=1
        print(f"Score: {score}")
    elif a == 'Is Python case-sensitive?' and answer == 'Yes':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which data type stores text?' and answer == 'str':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which data type stores whole numbers?' and answer == 'int':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which data type stores decimal numbers?' and answer == 'float':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which data type stores True or False?' and answer == 'bool':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'What is the output of print(5 + 3)?' and answer == '8':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'What is the output of print(10 // 3)?' and answer == '3':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'What is the output of print(10 % 3)?' and answer == '1':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which operator checks equality?' and answer == '==':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which operator means "not equal"?' and answer == 'not':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword is used for decision making?' and answer == 'if':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword is used when the first condition is false?' and answer == 'else':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword checks multiple conditions?' and answer == 'elif':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which loop repeats a fixed number of times?' and answer == 'for loop':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which loop runs while a condition is True?' and answer == 'while loop':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword exits a loop?' and answer == 'break':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword skips the current iteration?' and answer == 'continue':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function returns the length of a string or list?' and answer == 'len()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function converts a string to lowercase?' and answer == 'lower()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'What function converts a string to uppercase?' and answer == 'upper()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function removes whitespace from both ends of a string?' and answer == 'strip()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which operator is used for exponentiation in Python?' and answer == '**':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'What is the output of print(2 ** 3)?' and answer == '8':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function converts a string to an integer?' and answer == 'int()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function converts an integer to a string?' and answer == 'str()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function returns the type of a variable?' and answer == 'type()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword is used to define a function?' and answer == 'def':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword is used to return a value from a function?' and answer == 'return':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'What is the default return value of a function with no return statement?' and answer == 'None':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which data type is immutable: List or Tuple?' and answer == 'Tuple':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which brackets are used to create a list?' and answer == '[]':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which brackets are used to create a tuple?' and answer == '()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which brackets are used to create a dictionary?' and answer == '{}':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which brackets are used to create a set?' and answer == 'set()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which method adds an element to a list?' and answer == 'append()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which method removes the last element from a list?' and answer == 'pop()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which method sorts a list?' and answer == 'sort()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which method reverses a list?' and answer == 'reverse()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function finds the maximum value in a list?' and answer == 'max()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function finds the minimum value in a list?' and answer == 'min()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function calculates the sum of a list?' and answer == 'sum()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which function sorts without modifying the original list?' and answer == 'sorted()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which keyword is used to create a class?' and answer == 'class':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")

    elif a == 'Which special method acts as a constructor in Python?' and answer == '__init__()':
        print(f"Question: {a}")
        print(f"Answer: {answer}")
        score += 1
        print(f"Score: {score}")
    else:
        print(f"Question: {a}")
        print(f"Wrong Answer: {answer}")
print(f"Final Score: {score}")

	





