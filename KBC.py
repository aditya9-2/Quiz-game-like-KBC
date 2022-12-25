name = input("Enter Your name: ")
print("wellcome to KBC", name)
print("\n")

print('''RULES: You will be asked 3 questions.
 if you are able to give 3 correct answers
 you will get RS. 15,000/-''')
print("*************************************\n")

questions = [
    'A. Who developed Python Programming Language?',
    'B. What is the correct syntax to output "Hello World" in Python?',
    'C. How do you insert COMMENTS in Python code?'
]

options = [[
    "1) Wick Van Rossum", "2) Rasums Lerdorf", "3) Guido van Rossum",
    "4) Niene Stom"
],
    [
    '1) echo Hello World', '2)print("Hello World")',
    '3) const "Hello World"', "4) None of these"
],
    [
    "/*This is comment*/", "#This is Comment", "//This is comment",
    "COM -- This is comment"
]]

ans = [3, 2, 2]
amount = []

for i in range(len(questions)):
    while True:
        if i >= len(questions):
            break
        else:
            print("Answer the question:\n")
            print(questions[i])

            for a in options[i]:
                print(" " + a)
            sub = int(input("Enter Your Option: "))

            if sub == ans[i]:
                amount.append(5000)
                print("Correct Answer! You Got RS.", sum(amount))
                break
            else:
                print("Wrong Answer!\n")
                break

print("\nConragtulations", name, " You Just Won The Total Amount of RS. ",
      sum(amount))
