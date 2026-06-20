# 5 задач на ООП (магические методы)

Небольшие головоломки: «как заставить Python делать то, что обычно нельзя?»  
Ответ — переопределить магические методы: `__add__`, `__mul__`, `__eq__`, `__contains__` и др.

**Как работать:**

```
cd lesson-oop
py task-1.py   # тесты внизу файла — должны пройти без ошибок
py task-2.py
...
```

Подсказки — в каждом `task-N.py`. **Решения** — в папке `solutions/` или ниже в этом файле.

```
py solutions/task-1.py   # проверить готовое решение
```

---

## Задача 1. Как сложить строку с числом?

**Файл:** `task-1.py`

Обычно `"Мне " + 13` — **ошибка**. Сделайте класс `Text`, чтобы работало:

```python
Text("Мне ") + 13        # → Text("Мне 13")
Text("Год: ") + 2025     # → Text("Год: 2025")
```

**Нужен метод:** `__add__`

**Подсказка:** превратите `other` в строку через `str(other)`.

---

## Задача 2. Как сложить строку со списком?

**Файл:** `task-2.py`

```python
Text("abc") + ["d", "e", "f"]   # → Text("abcdef")
Text("") + [1, 2, 3]            # → Text("123")
```

**Нужен метод:** `__add__` (проверьте тип `other` через `isinstance`)

**Подсказка:** пройдите по списку и склеивайте элементы как строки.

---

## Задача 3. Как умножить «слово» на число?

**Файл:** `task-3.py`

Как `"ля" * 3` → `"ляляля"`, но для своего класса:

```python
Word("ля") * 3      # → Word("ляляля")
Word("Ha") * 2      # → Word("HaHa")
3 * Word("!")       # → Word("!!!")   ← число слева!
```

**Нужны методы:** `__mul__` и `__rmul__`

---

## Задача 4. Как сравнить две точки?

**Файл:** `task-4.py`

```python
Point(1, 2) == Point(1, 2)   # True
Point(0, 0) == Point(1, 0)   # False
Point(3, 4) == "точка"       # False (не падает с ошибкой)
```

**Нужен метод:** `__eq__`

**Подсказка:** если `other` не `Point`, верните `False`.

---

## Задача 5. Как проверить «есть ли в коробке?»

**Файл:** `task-5.py`

Как `"a" in [1, 2, 3]`, но для своего класса:

```python
box = Box(["яблоко", "груша", "банан"])
"груша" in box      # True
"апельсин" in box   # False
```

**Нужен метод:** `__contains__`

**Подсказка:** `"x" in box` вызывает `box.__contains__("x")`.

---

## Сводка

| № | Вопрос | Метод |
|---|--------|-------|
| 1 | строка + число | `__add__` |
| 2 | строка + список | `__add__` |
| 3 | слово × число | `__mul__`, `__rmul__` |
| 4 | точка == точка | `__eq__` |
| 5 | предмет in коробка | `__contains__` |

---

## Решения

### Задача 1

**Вариант А** — свой класс с `self.value`:

```python
class Text:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        # Text(...) — создаём новый объект, как Text("Мне 13")
        return Text(self.value + str(other))
```

**Вариант Б** — наследование от `str`, переопределение `__add__`:

```python
class Text(str):
    """Text — это str, но умеет складываться с числом."""

    def __add__(self, other):
        # super() — обращение к базовому классу str
        # str.__add__ умеет только str + str, поэтому other → str(other)
        return Text(super().__add__(str(other)))
```

Файл с тестами: `solutions/task-1-from-str.py`

| | Вариант А | Вариант Б |
|---|-----------|-----------|
| Данные | в `self.value` | сам объект **и есть** строка |
| `isinstance(t, str)` | False | True |
| Идея | обёртка вокруг строки | «улучшенная» строка |

### Задача 2

```python
class Text:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, list):
            extra = "".join(str(x) for x in other)
            return Text(self.value + extra)
        return Text(self.value + str(other))
```

### Задача 3

```python
class Word:
    def __init__(self, text):
        self.text = str(text)

    def __str__(self):
        return self.text

    def __mul__(self, n):
        return Word(self.text * int(n))

    def __rmul__(self, n):
        return self * n
```

### Задача 4

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
```

### Задача 5

```python
class Box:
    def __init__(self, items):
        self.items = list(items)

    def __contains__(self, item):
        return item in self.items
```

Полные файлы с тестами: `solutions/task-1.py` … `solutions/task-5.py`  
Задача 1 (наследование от `str`): `solutions/task-1-from-str.py`
