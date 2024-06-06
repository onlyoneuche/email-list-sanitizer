This Python script is designed to extract email addresses from a CSV file, remove duplicates, and write the cleaned data to a new CSV file. The script follows a modular design and incorporates several design patterns to promote code reusability, flexibility, and maintainability.

## Features

- Extracts email addresses from CSV rows using regular expressions
- Handles rows with multiple email addresses
- Removes duplicate email addresses
- Writes cleaned data to a new CSV file, with one email address per row

## Design Patterns

The script incorporates the following design patterns:

1. **Strategy Pattern**: The `EmailExtractor` class and its concrete implementation `RegexEmailExtractor` follow the Strategy pattern, allowing for different email extraction strategies to be used interchangeably. This pattern promotes flexibility and extensibility, as new email extraction algorithms can be easily added without modifying the existing code.

2. **Singleton Pattern**: The `EmailExtractorSingleton` class follows the Singleton pattern, ensuring that only one instance of the email extractor is created and shared throughout the application. This pattern promotes efficient resource usage and prevents unnecessary object creation.

3. **Facade Pattern**: The `EmailProcessingFacade` class provides a simplified interface for email extraction and CSV processing, hiding the complexities of the underlying implementation from the client code. This pattern promotes code clarity and ease of use, as the client code only needs to interact with the facade class.

## Usage

1. Import the necessary modules and classes.
2. Create an instance of the `EmailProcessingFacade` class, providing the input and output file paths.
3. Call the `process_csv` method on the facade instance to initiate the email extraction and CSV processing.

Example:

```python
input_file = "peter_hni.csv"
output_file = "peter_hni_processed.csv"
facade = EmailProcessingFacade(input_file, output_file)
facade.process_csv()
```

After running the script, the processed CSV file will be available at the specified output file path.

## Dependencies

- Python 3.x
- `csv` module (included in Python's standard library)
- `re` module (included in Python's standard library)

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).