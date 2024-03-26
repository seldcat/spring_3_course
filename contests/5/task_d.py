from abc import ABC, abstractmethod


class MetricBase(ABC):
    @abstractmethod
    def calculate(self, vector1: list[float], vector2: list[float]) -> float:
        pass

    @staticmethod
    def create(metric_type: str):
        if metric_type == "euclidean":
            return EuclideanMetric()
        elif metric_type == "manhattan":
            return ManhattanMetric()
        raise ValueError("Unknown metric type")

    @staticmethod
    def read_vector() -> list[float]:
        return list(map(float, input().split()))


class EuclideanMetric(MetricBase):
    def calculate(self, vector1: list[float], vector2: list[float]) -> float:
        return sum((x - y) ** 2 for x, y in zip(vector1, vector2)) ** 0.5


class ManhattanMetric(MetricBase):
    def calculate(self, vector1: list[float], vector2: list[float]) -> float:
        return sum(abs(x - y) for x, y in zip(vector1, vector2))


def main() -> None:
    metric_type = input()
    metric = MetricBase.create(metric_type)
    print(metric.calculate(MetricBase.read_vector(), MetricBase.read_vector()))


if __name__ == "__main__":
    main()
