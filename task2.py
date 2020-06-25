import datetime
import string

try:


    #если всё пойдёт по пизде удастся локализовать очаг возгарания
    base = open("data.txt", "r")

    #начале работы пусть выдаёт список задач

    print ("Ваши задачи:")
    #ты знаешь циклы?
    list = base.readlines()
    for task in list:
        print(task)

    print("уважаемый сударь! Не будете ли вы столь лююбезны ввести для себя задачу")
    print("Дабы я мог запомнить её и напомнить вам о ней?\n"      )
    taskText = str(input())
    currentDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #это я сам не знал. нагуглил

    finalTask = currentDate + ' ' + taskText + '\n11'
    print(finalTask)



finally:
   if base:
      base.close()


#Это называется код лапша. Дальше разбираемся с вермишелью
