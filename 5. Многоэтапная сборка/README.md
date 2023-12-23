Multistage build
----

[Link](https://docs.docker.com/build/building/multi-stage/) to official docker guide

```bash
docker build -t service --rm .
```

```bash
docker run --rm service
```

```text
Running first-service
```

```bash
docker run --rm service second-service
```

```text
Running second-service
```




