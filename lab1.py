# Все эти функции объявить в классе. Создать объект и вывести значения функций
class myClass:
    def __init__(self, sentence, word, newWord):
        self.sentence = sentence
        self.word = word
        self.newWord = newWord

    # Написать функцию, которая проверяет, есть ли в предложении совпадающие слова
    def check(self):
        return(bool(self.word in self.sentence)) 

    # Написать функцию, которая заменяет в предложении одно слово на другое
    def replace(self):
        #Продемонстрировать композицию двух функций
        if self.check():
            return self.sentence.replace(self.word, self.newWord)
        else:
            return "Word not found"


sentence = "Hello World" 
word = "World"
newWord = "George"

obj = myClass(sentence, word, newWord)
print(obj.check())
print(obj.replace())


# Реализовать функцию по п.2.2  рекурсивно
print("replacing "+ word +" with "+ newWord +" in "+  sentence + " gives: " +  obj.replace())

#Написать скрипт для ввода целого числа нахождения корня степени 1/3
def cube_root(x):
    if 0<=x: return x**(1./3.)
    return -(-x)**(1./3.)

print(cube_root(63))
