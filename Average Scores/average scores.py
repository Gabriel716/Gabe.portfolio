#Gabriel Harrison
#9/17
def average_scores():
    score1=float(input("What is your first score?"))           
    score2=float(input("What is your second score?"))
    score3=float(input("What is your third score?"))
    score4=float(input("What is your fourth score?"))
    score5=float(input("What is your fifth score?"))
    score6=float(input("What is your sixth score?"))
    score7=float(input("What is your seventh score?"))
    score8=float(input("What is your eighth score?"))
    score9=float(input("What is your ninth score?"))
    score10=float(input("What is your 10th score?"))
    all_scores=score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10 
    avg_scores=all_scores/10
    return avg_scores

              
print(average_scores())
                  
average_scores()
