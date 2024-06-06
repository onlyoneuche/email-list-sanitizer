import csv
import re
from abc import ABC, abstractmethod

# Strategy Pattern: Interface for email extraction strategies
class EmailExtractor(ABC):
    @abstractmethod
    def extract_emails(self, text):
        pass

# Strategy Pattern: Concrete implementation using regular expressions
class RegexEmailExtractor(EmailExtractor):
    def extract_emails(self, text):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, text)

# Singleton Pattern: Ensure a single instance of the email extractor
class EmailExtractorSingleton(object):
    _instance = None

    def __new__(cls, extractor=RegexEmailExtractor()):
        if cls._instance is None:
            cls._instance = super(EmailExtractorSingleton, cls).__new__(cls)
            cls._instance.extractor = extractor
        return cls._instance

    def extract_emails(self, text):
        return self.extractor.extract_emails(text)

# Facade Pattern: Simplified interface for email extraction and CSV processing
class EmailProcessingFacade:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.email_extractor = EmailExtractorSingleton()

    def process_csv(self):
        seen_emails = set()
        with open(self.input_file, 'r', newline='') as infile, open(self.output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            # Write the header row (assuming the header exists)
            writer.writerow(next(reader))
            for row in reader:
                cleaned_emails = []
                for element in row:
                    emails_from_element = self.email_extractor.extract_emails(element)
                    cleaned_emails.extend([email for email in emails_from_element if email not in seen_emails])
                    seen_emails.update(emails_from_element)
                for additional_email in cleaned_emails:
                    writer.writerow([additional_email])
        print("CSV processed successfully! Check", self.output_file)

# Usage
input_file = "peter_hni.csv"
output_file = "peter_hni_processed.csv"
facade = EmailProcessingFacade(input_file, output_file)
facade.process_csv()