import re

def arithmetic_arranger(problems, solve = False): #false is an optional parameter, this implies the output should display the result of calculation

  if (len(problems) > 5): #check how many problems we have
    return "Error: Too many problems."

  first = "" #first number
  second = "" #second number
  lines = ""
  sumx = ""
  string = ""

  for problem in problems: #loop through
    if(re.search("[^\s0-9.+-]", problem)): #look for digits
      if(re.search("[/]", problem) or re.search("[*]", problem)): #search for division or multiplication
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstNumber = problem.split(" ")[0] #split by space, 0 is 
    operator = problem.split(" ")[1] #second item will be the operator after the space
    secondNumber = problem.split(" ")[2]

    if(len(firstNumber) >= 5 or len(secondNumber) >= 5): #checking length of input
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if(operator == "+"):
      sum = str(int(firstNumber) + int(secondNumber)) #doing actual conversion based on operator being + sign
    elif(operator == "-"):
      sum = str(int(firstNumber) - int(secondNumber))

    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length) #rjust is right justified
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = "" # -----
    res = str(sum).rjust(length) #result
    for s in range (length):
      line += "-"

    if problem != problems[-1]: #-1 means last character. Put the spaces to seperate each problem
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx +=  res

  if solve: # we will display the result of . Outside of for loop
    string = first + "\n" + second + "\n" + lines + "\n" +sumx #display result
  else:
    string = first + "\n" + second + "\n" + lines #do not display result
  return string

