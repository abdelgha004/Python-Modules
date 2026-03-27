from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract base class for all data processors."""
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return a formatted result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the input data."""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatting (can be overridden)."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric lists."""

    def validate(self, data: Any) -> bool:
        """Return True if data is a list of numbers."""
        if isinstance(data, (int, float)):
            return True
        elif (isinstance(data, list)
              and all(isinstance(x, (int, float)) for x in data)
              and len(data) > 0):
            return True
        return False

    def process(self, data: Any) -> str:
        """Compute count, sum, and average of numeric data."""

        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        numbers: List[Union[int, float]] = data
        if isinstance(data, (int, float)):
            numbers = [data]
        else:
            numbers = data

        total = sum(numbers)
        count = len(numbers)
        avg = total / count

        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor for text strings."""

    def validate(self, data: Any) -> bool:
        """Return True if data is a string."""
        return isinstance(data, str) and len(data.strip()) > 0

    def process(self, data: Any) -> str:
        """Count characters and words in text."""

        if not self.validate(data):
            raise ValueError("Invalid text data")
        text: str = data
        char_count = len(text)
        word_count = len(text.split())

        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def validate(self, data: Any) -> bool:
        """Return True if data is a string."""
        return isinstance(data, str) and ": " in data

    def process(self, data: Any) -> str:
        """Extract log level and message, then format output."""
        if not self.validate(data):
            raise ValueError("Invalid log data")
        log: str = data
        level, message = log.split(": ", 1)

        level = level.strip().upper()
        message = message.strip()

        level_map: Dict[str, str] = {
            "ERROR": "[ALERT]",
            "INFO": "[INFO]",
            "WARNING": "[WARN]"
            }
        prefix = level_map.get(level, "[UNKNOWN]")

        return f"{prefix} {level} level detected: {message}"


def process_data(processor: DataProcessor, data: Any) -> None:
    """Helper function to process data with a given processor."""
    try:
        print(f"Processing data: {data}")
        if not processor.validate(data):
            raise ValueError("Data validation failed")

        if isinstance(processor, NumericProcessor):
            print("Validation: Numeric data verified")
        elif isinstance(processor, TextProcessor):
            print("Validation: Text data verified")
        elif isinstance(processor, LogProcessor):
            print("Validation: Log entry verified")

        result: Optional[str] = None
        result = processor.process(data)
        print(processor.format_output(result))
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Run processor demos and polymorphic example."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric_data = [1, 2, 3, 4, 5]
    process_data(NumericProcessor(), numeric_data)

    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    process_data(TextProcessor(), text_data)

    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    process_data(LogProcessor(), log_data)

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")

    processing_tasks = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "testing code"),
        (LogProcessor(), "INFO: System ready")
    ]

    for index, (processor, input_data) in enumerate(processing_tasks, start=1):
        try:
            result = processor.process(input_data)
            print(f"Result {index}: {result}")
        except Exception as e:
            print(f"Result {index}: Error: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
