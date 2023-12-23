Основной единицей логики докера является контейнер (container).
Контейнер это некоторый запущенный процесс, работающий в своем приватном окружении.
Контейнер обладает своей файловой системой, своим набором процессов и своей локальной сетью.

Для запуска контейнера необходимо выбрать образ (image). Образ это сформированное окружение файловой системы \
которую будет использовать конетйнер.

Начнем с запуска тестового образа `hello-world`. Для запуска контенера используется команда `docker run <image id>`
Выполним команду.
```bash
docker run hello-world
```
И после некоторого времени получим примерно следующий ответ.

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete 
Digest: sha256:c79d06dfdfd3d3eb04cafd0dc2bacab0992ebc243e083cabe208bac4dd7759e0
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Здесь мы видим что докер не смог найти образ локально и выгрузил его из официального репозитория.
Далее видими результат работы контейнера: фраза приветствия и некоторая вспомогательная информация.

Для просмотра существующих контейнеров используется команда `docker ps -a`. Флаг `-a` (all) означает
показ всех существующих конетейнеров, а не только работающих.

Вывод команды примерно следующий:
```
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS   NAMES
868424a3d12d   hello-world   "/hello"   11 minutes ago   Exited (0) 11 minutes ago           trusting_chatterjee
```

Мы видим уникальный индентификатор контейнера, название образа, потомком которого он является, команда запущенная \
в нем (про это позже), время созания, статус, проброшенные порты и имя. \
На данный момент важным для нас является стасут, который указывает на то, что контейнер завершился с успехом и уникальное имя \
конейтнера, которое в данном случае генерируется автоматически.

Ссылки:
- [Запуск первого образа докера (подробнее)](https://habr.com/ru/articles/584820/)
