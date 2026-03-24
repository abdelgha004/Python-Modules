from typing import Any, Tuple
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

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
        return (
            isinstance(data, list)
            and all(isinstance(x, (int, float)) for x in data)
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        total = sum(data)
        count = len(data)
        avg = total / count if count else 0

        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor for text strings."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        char_count = len(data)
        word_count = len(data.split())

        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        level, message = data.split(": ", 1)
        level = level.strip()
        message = message.strip()

        if level == "ERROR":
            prefix = "[ALERT]"
        elif level == "INFO":
            prefix = "[INFO]"
        else:
            prefix = "[UNKNOWN]"

        return f"{prefix} {level} level detected: {message}"


def main() -> None:
    """Run processor demos and polymorphic example."""

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("\nInitializing Numeric Processor...")

    num = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    try:
        print(f"Processing data: {numeric_data}")
        if num.validate(numeric_data):
            print("Validation: Numeric data verified")
            result = num.process(numeric_data)
            print(num.format_output(result))
    except Exception as e:
        print(f"Error: {e}")

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    text_data = "Hello Nexus World"
    try:
        print(f"Processing data: \"{text_data}\"")
        if text.validate(text_data):
            print("Validation: Text data verified")
            result = text.process(text_data)
            print(text.format_output(result))
    except Exception as e:
        print(f"Error: {e}")

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    log_data = "ERROR: Connection timeout"
    try:
        print(f"Processing data: \"{log_data}\"")
        if log.validate(log_data):
            print("Validation: Log entry verified")
            result = log.process(log_data)
            print(log.format_output(result))
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")

    processing_tasks = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "testing codes"),
        (LogProcessor(), "INFO: System ready")
    ]

    for index, (processor, input_data) in enumerate(processing_tasks, start=1):
        try:
            result = processor.process(input_data)
            print(f"Result {index}: {result}")
        except Exception as e:
            print(f"Result {index}: Error - {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
