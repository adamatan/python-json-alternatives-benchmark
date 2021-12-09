# Python JSON Benchmark
[![Test, Lint, Build and Push to ECR](https://github.com/adamatan/python-json-benchmark/actions/workflows/benchmark.yaml/badge.svg)](https://github.com/adamatan/python-json-benchmark/actions)

# How to Run
Clone the repo and run:

    make

That's it. The only requirements are Docker and Make.

## Results - TL;DR
[`orjson`](https://github.com/ijl/orjson) is the fastest JSON library tested.


## Full results
The raw results are available under the [actions tab](https://github.com/adamatan/python-json-benchmark/actions). Pick the latest invocation, click `benchamrk` and exapand `Benchmark`.

The latest results from [the Github Actions virtual machine](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners) are:

### Long JSON text dumps()
```bash
+-----------+---------------+----------------------+----------+-----------------+
|  Library  | Functionality | Number of Iterations | Duration | Invocations/sec |
+-----------+---------------+----------------------+----------+-----------------+
|   orjson  |   dumps_test  |         1000         |  0.23s   |     4329.67     |
|   ujson   |   dumps_test  |         1000         |  0.57s   |     1747.10     |
| rapidjson |   dumps_test  |         1000         |  0.88s   |     1133.41     |
|    json   |   dumps_test  |         1000         |  1.08s   |      926.46     |
+-----------+---------------+----------------------+----------+-----------------+
```

### Short JSON text dumps()
```bash
+-----------+---------------+----------------------+----------+-----------------+
|  Library  | Functionality | Number of Iterations | Duration | Invocations/sec |
+-----------+---------------+----------------------+----------+-----------------+
|   orjson  |   dumps_test  |       1000000        |  1.08s   |    923067.56    |
| rapidjson |   dumps_test  |       1000000        |  3.42s   |    292287.32    |
|   ujson   |   dumps_test  |       1000000        |  3.50s   |    285403.04    |
|    json   |   dumps_test  |       1000000        |  7.77s   |    128689.84    |
+-----------+---------------+----------------------+----------+-----------------+
```

### Long JSON text loads()
```bash
+-----------+---------------+----------------------+----------+-----------------+
|  Library  | Functionality | Number of Iterations | Duration | Invocations/sec |
+-----------+---------------+----------------------+----------+-----------------+
|   orjson  |   loads_test  |         1000         |  0.52s   |     1912.31     |
|   ujson   |   loads_test  |         1000         |  0.71s   |     1399.71     |
|    json   |   loads_test  |         1000         |  0.84s   |     1195.51     |
| rapidjson |   loads_test  |         1000         |  1.01s   |      989.86     |
+-----------+---------------+----------------------+----------+-----------------+
```

### Short JSON text loads()
```bash
+-----------+---------------+----------------------+----------+-----------------+
|  Library  | Functionality | Number of Iterations | Duration | Invocations/sec |
+-----------+---------------+----------------------+----------+-----------------+
|   orjson  |   loads_test  |       1000000        |  2.73s   |    366076.18    |
|   ujson   |   loads_test  |       1000000        |  3.73s   |    267983.03    |
| rapidjson |   loads_test  |       1000000        |  4.32s   |    231691.96    |
|    json   |   loads_test  |       1000000        |  5.89s   |    169906.22    |
+-----------+---------------+----------------------+----------+-----------------+
```
