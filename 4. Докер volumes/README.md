До этого моменты наши контейнеры не сохраняли никакой информации на файловую систему хоста (операционной системой пользователя).
Контейнеры использовали свобственную приватную фаловую систему, которая удалялась вместе с контейнером.
Для возможности работать с файловой системой хоста используются докер [volumes](https://docs.docker.com/storage/volumes/).


Один из случаев использования волюмов это сохранение данных работы контейнера.
Для демонстрации работы предлагается собрать образ контейнера, корый будет обновлять
данные в директории которая предоставлена ему как волюм.
Для сборки используется следующая команда:

```
docker build -t writer .
```

Далее запустим писателя: 

```
docker run -v "$(pwd)":/app --rm writer
```

и увидим что в текущей директории появился файл `file.json` со следующим содержимым:

```json
[
    {
        "launchNumber": 1
    }
]
```

При повторном запуске увидим что количество записей в файле обновляется.

```json
[
    {
        "launchNumber": 1
    },
    {
        "launchNumber": 2
    }
]
```

Давайте подробнее разберем почему так происходит. Вся магия в команде запуска конетйнера.
Мы использовали флаг `-v` который позволяет смонтировать любую директорию или файл в файловую систему контейнера.
Флаг имеет следющий синтакс: `-v <host file path>:<container file path>`.
В нашем случае мы монтируем текущую директорию (используем `pwd` так как путь должен быть абсолютным) в директорию `/app`
в контейнере.
С этого момента в контенере становятся доступными для изменения все файлы в текущей директории.

Часто мы не хоим следить за тем где хранятся данные, генерируемые контейнерами.
Для решения этой проблемы докер имеет встроенное хранилище волюмов. Волюм это некоторая часть файловой системы
которая монтируется как обычная папку, но храниться внутри докера.

В данном случае мы создаем волюм `myvolume` и монтируем его в папку `/app` внутри контейнера.

```bash
docker run -v myvolume:/app --rm writer
```

Теперь при повторный запусках мы увидим то же поведение контейнера что и раньше.
При первом запуске волюм создавался и был пуст. При повторных использовался ранее созданный волюм.

```bash
$ docker run -v myvolyme:/app --rm writer
Create file /app/file.json
$ docker run -v myvolyme:/app --rm writer
Append to /app/file.json
```

Для просмотра всех созданнх волюмов используется команда `docker volume ls`.

Увидим примерно следующий список созданнх волюмов.
Безымянные волюмы могут генерироваться в случае использовани команды `VOLUME` при сборке образа.

```
DRIVER    VOLUME NAME
local     0c83b56c5a8cf9b92441e7881e72caa7845d121ceec006337a4842d55776a917
local     99f492f7ad994e25b743a38194bd7353690f9635fa58b19d741bc8cd9b1b5298
local     426efa46b71980a4856986f1b1e1c953f14928e6a7506715f810f624a2cefe62
local     myvolyme
```

[Статья на хабре](https://habr.com/ru/companies/ruvds/articles/441574/)
[Официальная документация (очень подробная)](https://docs.docker.com/storage/volumes/)
