import requests
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.squad import Squad
from lab_python_oop.circle import Circle

# Функция для демонстрации методов всех созданных классов
def main():
    print("Версия библиотеки requests из виртуального окружения: " + requests.__version__ + "\n")

    rect = Rectangle(18,18, "Red")
    sqd = Squad(18,"Purple")
    circ = Circle(18, "Green")

    rect.about()
    sqd.about()
    circ.about()

    print("\n\033[33mИспользуя метод \033[35m__repr__\033[0m:")
    print(rect)
    print(sqd)
    print(circ)


if __name__ == "__main__":
    main()