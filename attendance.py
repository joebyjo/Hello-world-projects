class_held = int(input("Enter total number of classes held: "))
classes_attended = int(input('Enter total classes attended: '))
percentage = int(classes_attended / class_held * 100)
if percentage >= 75:
    print("your can write the exam")
else:
    print (('your percentage is ') + str(percentage) + (',so you can not write the exam'))
