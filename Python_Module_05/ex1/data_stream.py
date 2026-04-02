from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    """Abstract base class for all data streams."""
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.process_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter batch data based on a string criteria."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic statistics of the stream."""
        return {
            "stream_id": self.stream_id,
            "process_count": self.process_count
            }


class SensorStream(DataStream):
    """Processes sensor readings, detects extreme temperature alerts."""
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.process_count += len(data_batch)
            temp_values = [float(item.split(":")[1]) for item in data_batch
                           if "temp:" in item]
            avg_temp = (
                sum(temp_values) / len(temp_values)
                if temp_values else 0.0
                )
            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp}°C"
                )
        except Exception as e:
            return f"Sensor error: {e}"


class TransactionStream(DataStream):
    """Processes financial transactions (buy/sell) and computes net flow."""
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.process_count += len(data_batch)
            total: float = 0.0
            for item in data_batch:
                action, value_str = item.split(":")
                value = float(value_str)
                if action == "buy":
                    total += value
                elif action == "sell":
                    total -= value

            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {total:+} units"
                )
        except Exception as e:
            return f"Transaction error: {e}"


class EventStream(DataStream):
    """Processes system events and counts errors."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Processes system events and counts errors."""
        try:
            self.process_count += len(data_batch)
            error_count = sum(
                1 for item in data_batch if "error" in str(item).lower()
                )

            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{error_count} error detected"
                )
        except Exception as e:
            return f"Event error: {e}"


class StreamProcessor:
    """Handles multiple data streams polymorphically."""
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: list[list[Any]]) -> None:
        """Process each batch in each stream polymorphically."""
        for stream, batch in zip(self.streams, batches):
            try:
                if isinstance(stream, SensorStream):
                    print("\nInitializing Sensor Stream...")
                    print(f"Stream ID: {stream.stream_id}, "
                          "Type: Environmental Data")
                    print(f"Processing sensor batch: [{', '.join(batch)}]")
                elif isinstance(stream, TransactionStream):
                    print("\nInitializing Transaction Stream...")
                    print(f"Stream ID: {stream.stream_id}, "
                          "Type: Financial Data")
                    print(f"Processing transaction batch: "
                          f"[{', '.join(batch)}]")
                elif isinstance(stream, EventStream):
                    print("\nInitializing Event Stream...")
                    print(f"Stream ID: {stream.stream_id},"
                          " Type: System Events")
                    print(f"Processing event batch: [{', '.join(batch)}]")

                result = stream.process_batch(batch)
                print(result)
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")

    def display_batch_summary(self, batches: list[list[Any]]) -> None:
        """Prints a concise summary of all batches processed."""
        print("\nBatch 1 Results:")
        for stream, batch in zip(self.streams, batches):
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(batch)} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")

    def display_filtered_results(self) -> None:
        """Demonstrates filtering capabilities on streams."""
        print("\nStream filtering active: High-priority data only")
        sensor_alerts = self.streams[0].filter_data(
            ["temp:50", "temp:10", "temp:50"], "50"
            )
        large_transactions = self.streams[1].filter_data(
            ["buy:100", "sell:500", "buy:20"], "500"
            )
        print(
            f"Filtered results: {len(sensor_alerts)} critical sensor alerts, "
            f"{len(large_transactions)} large transaction")


def main() -> None:

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches__initial = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"]
    ]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    processor.process_all(batches__initial)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    batches = [
        ["temp:20", "temp:25"],
        ["buy:100", "sell:50", "sell:70", "buy:20"],
        ["login", "error", "logout"]
    ]

    processor.display_batch_summary(batches)
    processor.display_filtered_results()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
