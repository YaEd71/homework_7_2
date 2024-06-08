# Шаг 1: Создание и запись текста в файл
file_path = "poem.txt"
text = """
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.
"""

with open(file_path, "w", encoding="utf-8") as file:
    file.write(text)

# Шаг 2: Открытие файла в режиме чтения и вывод содержимого на консоль
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# Файл автоматически закрывается после выхода из блока with

print("Пример использования без 'with'")

file = open(file_path, "r", encoding="utf-8")
content = file.read()
print(content)
file.close()  # Не забудьте закрыть файл вручную!

