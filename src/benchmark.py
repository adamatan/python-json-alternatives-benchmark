"""
Benchmark comparing some JSON libraries in Python.

Copyright 2021 Adam Matan.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import json
from types import ModuleType
from typing import Callable

import orjson
import rapidjson  # type: ignore
import ujson

from prettytable import PrettyTable
from loguru import logger

import urllib.request


LONG_JSON_URL = "https://jsonplaceholder.typicode.com/comments"
SHORT_JSON_URL = "https://jsonplaceholder.typicode.com/users/1"


def get_raw_text_from_url(url: str, description: str) -> str:
    with urllib.request.urlopen(url) as url_object:
        data = url_object.read().decode()
        logger.success(f"Fetched {description} from {url}, {len(data)} characters")
    return data


SHORT_JSON_TEXT = get_raw_text_from_url(SHORT_JSON_URL, "Short JSON")
LONG_JSON_TEXT = get_raw_text_from_url(LONG_JSON_URL, "Long JSON")


def dumps_test(_, json_object: dict, json_library: ModuleType) -> str:  # type: ignore
    text_from_object: str = json_library.dumps(json_object)  # type: ignore
    return text_from_object


def loads_test(json_text: str, _, json_library: ModuleType) -> dict:  # type: ignore
    object_from_text = json_library.loads(json_text)  # type: ignore
    return object_from_text


def run_test(
    test_name: str, json_text: str, number_of_iterations: int, test_function: Callable
) -> None:
    report = PrettyTable(
        [
            "Library",
            "Functionality",
            "Number of Iterations",
            "Duration",
            "Invocations/sec",
        ]
    )
    for json_library in rapidjson, orjson, ujson, json:
        json_object_from_text = json.loads(json_text)
        start_time = time.monotonic()
        logger.info(
            f"{test_name}: {number_of_iterations} iterations "
            + f"{test_function.__name__} "
            + f"{json_library.__name__} "
        )
        for _ in range(number_of_iterations):
            test_function(json_text, json_object_from_text, json_library)
        duration = time.monotonic() - start_time
        invocations_per_second = number_of_iterations / duration
        report.add_row(
            [
                json_library.__name__,
                test_function.__name__,
                number_of_iterations,
                f"{duration:.2f}s",
                f"{invocations_per_second:.2f}",
            ]
        )
    report.sortby = "Duration"
    logger.success(f"{test_name}\n{report}")


run_test(
    test_name="Long JSON text dumps()",
    json_text=LONG_JSON_TEXT,
    number_of_iterations=1000,
    test_function=dumps_test,
)

run_test(
    test_name="Short JSON text dumps()",
    json_text=SHORT_JSON_TEXT,
    number_of_iterations=1000000,
    test_function=dumps_test,
)

run_test(
    test_name="Long JSON text loads()",
    json_text=LONG_JSON_TEXT,
    number_of_iterations=1000,
    test_function=loads_test,
)

run_test(
    test_name="Short JSON text loads()",
    json_text=SHORT_JSON_TEXT,
    number_of_iterations=1000000,
    test_function=loads_test,
)
