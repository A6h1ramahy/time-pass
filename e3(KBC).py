print("Welcome to 'Kaun Banega CarodPati' and BEST OF LUCK !!!")
print("""RULES : 
                -There will be 5 questions.
                -A question will be having 4 options.
                -Choose thhe correct answer and Enter the correct option.
                -Each correct answer will raise a price of 20 lakh.
                -And a single wrong answer will lead to end of the Game.
                -You will be winning a price of what you earned before giving a wrong answer.
                -You will be a Carodpati if you answer all the 5 questions correctly.""")

print("ARE YOU READY.......?!?!?!?!?!")
b=input("Enter YES or NO : ")

while b.lower()!="yes":
    print("""RULES : 
                -There will be 5 questions.
                -A question will be having 4 options.
                -Choose thhe correct answer and Enter the correct option.
                -Each correct answer will raise a price of 20 lakhs.
                -And a single wrong answer will lead to end of the Game.
                -You will be winning a price of what you earned before giving a wrong answer.
                -You will be a Carodpati if you answer all the 5 questions correctly.""")
    print()
    print("ARE YOU READY NOW..?!?!?!?")
    b=input("Enter YES or NO : ")

q1 = ["What is Capital City of INDIA ?","(1):BANGLORE","(2):MUMBAI","(3):DELHI","(4):HYDERABAD"]
q2 = ["What do humans primarily breathe in to survive ?","(1) Carbon Dioxide","(2) Oxygen", "(3) Nitrogen","(4) Helium"]
q3 = ["What is the national animal of India ?","(1) Elephant","(2) Tiger","(3) Lion","(4) Peacock"]
q4 = ["Which planet is known as the \"Red Planet\" ?","(1) Jupiter","(2) Venus","(3) Mars","(4) Saturn"]
q5 = ["Which of these is a primary color ?","(1) Green","(2) Yellow","(3) Red","(4) Pink"]

print("Your First Question is,")
print(q1[0])
print("OPTIONS are,")
for i in q1[1:]:
    print(i)
ans=int(input("Enter your answer (1/2/3/4) : "))
if ans!=3:
    print("""WRONG ANSWER !!!
          Better Luck Next time""")
else:
    print("CORRECT ANSWER !!!")
    print("You won 20 lakh")
    print("Your Second Question is,")
    print(q2[0])
    print("OPTIONS are,")
    for i in q2[1:]:
        print(i)
    ans=int(input("Enter your answer (1/2/3/4) : "))
    if ans!=2:
        print("""WRONG ANSWER !!! You are ending your KBC journey here...
              Congratulations
              You can collect 20 lakhs""")
    else:
        print("CORRECT ANSWER !!!")
        print("You won 20 lakh again making Total of 40 lakhs")
        print("Your Third Question is,")
        print(q3[0])
        print("OPTIONS are,")
        for i in q3[1:]:
            print(i)
        ans=int(input("Enter your answer (1/2/3/4) : "))
        if ans!=2:
            print("""WRONG ANSWER !!! You are ending your KBC journey here...
                  Congratulations
                  You can collect 40 lakhs""")
        else:
            print("CORRECT ANSWER !!!")
            print("You won 20 lakh again making Total of 60 lakhs")
            print("Your Fourth Question is,")
            print(q4[0])
            print("OPTIONS are,")
            for i in q4[1:]:
                print(i)
            ans=int(input("Enter your answer (1/2/3/4) : "))
            if ans!=3:
                print("""WRONG ANSWER !!! You are ending your KBC journey here...
                      Congratulations
                      You can collect 60 lakhs""")
            else:
                print("CORRECT ANSWER !!!")
                print("You won 20 lakh again making Total of 80 lakhs")
                print("Here is your 1 crore winning Question,")
                print(q5[0])
                print("OPTIONS are,")
                for i in q5[1:]:
                    print(i)
                ans=int(input("Enter your answer (1/2/3/4) : "))
                if ans!=3:
                    print("""WRONG ANSWER !!! You are ending your KBC journey here...
                          Congratulations
                          You can collect 80 lakhs""")  
                else:
                    print("CORRECT ANSWER !!!")
                    print("CONGRATULATIONS FOR YOUR SUCCESS....")
                    print("You won 1 CRORE ")
                    print("You are a CARODPATI noww.....!!!!!")