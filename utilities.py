import re
import csv
import sys

# Define regex pattern for log parsing
log_pattern = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ([A-Za-z0-9]+) - (ERROR|WARNING|WARN|INFO|DEBUG) - (.+)$"
)

def read_file(file_path):
    """Generator function to read a file line by line"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(404)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(404)
        
        
def process_logs(input_file):
    """Process log lines from a file and write valid and invalid entries to separate CSV files"""
    try:
        with open("valid_logs.csv", mode="w", newline="", encoding="utf-8") as valid_file, \
             open("invalid_logs.csv", mode="w", newline="", encoding="utf-8") as invalid_file:
            
            valid_writer = csv.writer(valid_file)
            invalid_writer = csv.writer(invalid_file)

            # Writing headers
            valid_writer.writerow(["Timestamp", "Service", "Log Level", "Message"])
            invalid_writer.writerow(["Invalid Log Line"])

            # Process log lines
            for log in read_file(input_file):
                if log:  # Ignore empty lines
                    match = log_pattern.match(log)
                    if match:
                        valid_writer.writerow(match.groups())
                    else:
                        invalid_writer.writerow([log])

        print("Log processing complete. Check 'valid_logs.csv' and 'invalid_logs.csv'.")
    
    except Exception as e:
        print(f"Error processing logs: {e}")
        sys.exit(404)

# Example Usage:
# process_logs("app.log")
