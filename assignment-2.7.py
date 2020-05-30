score = float(input("Enter score between 0.0 and 1.0: "))
if score>1.0 or score<0.0 :
    print("error")
elif score>=0.9 :
    print('A grade')
elif score>=0.8 :
    print('B grade')
elif score>=0.7 :
    print('C grade')
elif score>=0.6 :
    print('D grade')
else :
    print('F grade') 
