# Тест "Трехцветый человек"

## Описание проекта
Программная версия теста по определению цвета человека: синего, красного, зеленого.

Программа написана на языке Python версии 3.12.2, для визуализации выбрана библиотека PySimpleGUI, которая позволяет быстро и просто создать интерфейс, и библиотека matplotlib для отображения результатов теста в виде круговой диаграммы.

## Как установить и запустить проект
Для простой установки создан exe-файл, который можно скачать [по ссылке](https://drive.google.com/file/d/1Zor9XyL8K4l83nvoBIqnU5ytxgCKjK0V/view?usp=sharing).

### Второй способ.
Клонируем репозиторий и перейдем в папку с тестом.
```bash
git clone https://github.com/EkaterinaKugot/TheTricolorMan.git
cd */TheTricolorMan
```

Установим необходимые библиотеки. 
```bash
pip install matplotlib
pip install PySimpleGUI
```

Запустим тест на определения цвета.
```bash
python main.py
```

Для запуска тестов можно докачать фреймворк pytest.
```bash
pip install pytest
```

Для просмотра покрытия тестов можно докачать coverage.
```bash
pip install coverage
```
 
Просмотр покрытия тестов.
```bash
coverage run -m pytest
coverage html
```

После запуска команд открываем папку htmlcov и файл index.html.

## Инструкция по прохождению теста.
Отвечая на вопросы, следует выбрать из трех ответов один. 
– Если у вас есть сомнения, выберите просто наиболее подходящий для вас ответ.
Тот или иной ответ не говорит о том, что вы лучше или хуже, а просто о том, что вы тот или иной.

## Контактная информация
:wink:EkaterinaKugot - ekel.kugot@gmail.com 

## Лицензия
MIT



