FROM nvidia/cuda:12.0.0-devel-ubuntu22.04 as build

RUN apt update && \
    apt install -y cmake

WORKDIR /app

COPY CMakeLists.txt .
COPY main.cu .

RUN cmake -B build && \
    cmake --build build

FROM nvidia/cuda:12.0.0-runtime-ubuntu22.04

WORKDIR /app

COPY --from=build /app/build/main .

ENTRYPOINT ["./main"]
