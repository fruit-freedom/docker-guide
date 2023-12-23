


[Официальный репозиторий с CUDA образами](https://hub.docker.com/r/nvidia/cuda/tags)

[Cmake CUDA guide](https://developer.nvidia.com/blog/building-cuda-applications-cmake/)


Для возможности работы с GPU из контейнера необходимо установить следующий
[пакет](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
> Обязательно после установки перезапустите докер демона `sudo systemctl restart docker`.

Также при запуске контейнера необходимо передать специальный флаг `--gpus`, который регулирует количество девайсов
с которыми может взаимодействовать контейнер.


```
docker run --rm --gpus all cuda_vector_add
```

