import datetime
import string

try:
    #ты знаешь функции?
    def printTasks(file):
        list = file.readlines()
        for task in list:
            print(task)

    def takeTask(file):
        print("уважаемый сударь! Не будете ли вы столь лююбезны ввести для себя задачу")
        print("Дабы я мог запомнить её и напомнить вам о ней?\n"      )
        taskText = str(input())
        return saveToFile(file, taskText)

    def saveToFile(file, text):
        currentDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        finalTask = currentDate + ' ' + text + '\n'
        file.write(finalTask)
        return  finalTask

    #если всё пойдёт по пизде удастся локализовать очаг возгарания
    base = open("data.txt", "r+")

    #начале работы пусть выдаёт список задач

    print ("Ваши задачи:")
    printTasks(base)


    finalTask = takeTask(base)

    print(finalTask)



finally:
   if base:
      base.close()


#дальше коммады
