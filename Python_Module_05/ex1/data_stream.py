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
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.process_count += len(data_batch)
            total: float = 0.0
            for item in data_batch:
                action, valuo_str = item.split(":")
                value = float(valuo_str)
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
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

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
                result = stream.process_batch(batch)
                print(result)
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    # Sensor Stream
    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_data)}]")
    print(sensor.process_batch(sensor_data))

    # Transaction Stream
    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print("Stream ID: TRANS_001, Type: Financial Data")
    transaction_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(transaction_data)}]")
    print(transaction.process_batch(transaction_data))

    # Event Stream
    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print("Stream ID: EVENT_001, Type: System Events")
    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_data)}]")
    print(event.process_batch(event_data))

    # Polymorphic processing with StreamProcessor
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    streams: List[DataStream] = [sensor, transaction, event]

    processor = StreamProcessor()
    for s in streams:
        processor.add_stream(s)

    batches = [
        ["temp:20", "temp:25"],
        ["buy:100", "sell:50", "sell:70", "buy:20"],
        ["login", "error", "logout"]
    ]

    print("\nBatch 1 Results:")
    for stream, batch in zip(processor.streams, batches):
        _ = stream.process_batch(batch)
        if isinstance(stream, SensorStream):
            print(f"- Sensor data: {len(batch)} readings processed")
        elif isinstance(stream, TransactionStream):
            print(f"- Transaction data: {len(batch)} operations processed")
        elif isinstance(stream, EventStream):
            print(f"- Event data: {len(batch)} events processed")

    print("\nStream filtering active: High-priority data only")
    filter_sensor = sensor.filter_data(["temp:50", "temp:10", "temp:50"], "50")
    filter_transaction = transaction.filter_data(
        ["buy:100", "sell:500", "buy:20"], "500"
        )
    print(
        f"Filtered results: {len(filter_sensor)} critical sensor alerts, "
        f"{len(filter_transaction)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
