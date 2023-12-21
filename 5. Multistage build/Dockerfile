FROM ubuntu:22.04 as build

RUN apt update && \
    apt install -y cmake build-essential

WORKDIR /app

COPY CMakeLists.txt .
COPY main.cpp .

RUN cmake -B build && \
    cmake --build build

FROM ubuntu:22.04

WORKDIR /app

COPY --from=build /app/build/service .

ENTRYPOINT ["/app/service"]

CMD ["first-service"]
