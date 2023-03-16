# IF
# OPERATORI LOGICI AND e OR


x = 12

if 10 < x < 20:
    print("compreso tra 10 e 20")
    
if x > 10 and x < 20:
    print("compreso tra 10 e 20 con AND che indica che vuole entrambe le condizioni come verificate")
    
    
y = 5

if x == 10 or y == 5:
    print("condizione verificata perchè almeno una delle due condizioni è vera")
else:
    print("nessuna delle condizioni è verificata")