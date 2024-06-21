# Виджет для банковских операций

Этот проект представляет собой виджет для выполнения различных банковских операций.

## Структура проекта

├── src
│ ├── masks.py
│ ├── processing.py
│ ├── widget.py
│ └── generators.py
├── tests
├── test_masks.py
├── test_processing.py
├── test_widget.py
└── test_generators.py



### Модули

- **masks.py**
- **processing.py**
- **widget.py**
- **generators.py**
- 
## Установка

1. Клонируйте репозиторий:

   git clone https://github.com/Mmclinks/homework_10_2.git
2. Установите зависимости:

pip install
poetry install

Тестирование
Запустите тесты с помощью pytest:

pytest

Покрытие кода:

File	            statements	missing	 excluded  coverage
src/__init__.py	    0	        0	     0	       100%
src/generators.py	11	        0	     0	       100%
src/masks.py	    17	        0	     0	       100%
src/processing.py	8	        0	     0         100%
src/widget.py	    24	        2	     0	       92%
Total	            60	        2	     0	       97%

Лицензия:

Этот проект лицензирован по [лицензии MIT].

Этот README.md файл предоставляет информацию о проекте, его 
структуре, установке, использовании, тестировании и лицензии.
