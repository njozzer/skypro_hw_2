# Проект Домашнее задание
### **Установка:**

1. **Клонируйте проект** с этого репозитория, используя в PyCharm (в командной строке терминала) команду:
```
git clone https://github.com/njozzer/skypro_hw_2.git
```
2. **Инициализируйте виртуальное окружение** командой:
```
python -m venv <название_окружения>
```
*Например:*
```
python -m venv venv
```
3. **Активируйте окружение** с помощью команды:
*   на macOS и Linux:
```
source venv/bin/activate
```
*   на Windows:
```
venv\Scripts\activate
```
4. **Установите все зависимости проекта** (указанные в файле `requirements.txt`) командой:
```
pip install -r requirements.txt
```
4. **Установите линтеры**:
```
poetry install
```
### **Модули:**
```
src/utils
```
Класс категорий
```
src/Category
```
Класс продуктов
```
src/Product
```
### **Тестирование:**
Протестировать модули можно через команды:
```
python -m pytest
```
или
```
python -m pytest --cov=src --cov-report=html
```