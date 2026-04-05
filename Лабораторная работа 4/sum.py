# TODO решите задачу
import json


def task() -> float:
    name = "input.json"
    with open(name) as f:
        data = json.load(f)

    summ = sum([item["score"] * item["weight"] for item in data])
    return round(summ, 3)


print(task())
