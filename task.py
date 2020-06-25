import string, datetime
#не надо столько комментариев
#f = open("1.txt", "a")
base = open("data.txt", "a")
#внятные имена
#дружественный интерфейс
print("уважаемый сударь! Не будете ли вы столь лююбезны ввести для себя задачу")
print("Дабы я мог запомнить её и напомнить вам о ней?\n"      )
taskText = str(input())
#f.tell() нафига? всё равно в конец запишет
#datetime.date(int(2020), int(6), int(3)) комп сам знает время. Не делай за него его работу
currentDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #это я сам не знал. нагуглил
#print('datatime'+'\n' + 'x') ну почти, только без кавычек
finalTask = currentDate + ' ' + taskText + '\n11'
print(finalTask)
base.write(finalTask)

#осталось по просьбе выдавать задачи
#как минимум надо закрыть файл


