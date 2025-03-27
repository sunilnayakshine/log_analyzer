
# Log Analyzer

This Log Analyzer processes log files, extracts relevant information, and generates statistical reports. It supports grouping logs by service, log level, and messages, while also handling invalid log entries separately.

## Features

-   Extracts valid log entries and saves them to `valid_logs.csv`.
    
-   Identifies invalid log entries and saves them to `invalid_logs.csv`.
    
-   Supports various statistics:
    
    -   Group logs by log level.
        
    -   Group logs by service.
        
    -   Group logs by common messages.
        
    -   Retrieve invalid log entries.
        
-   Ensures that `--dataload` is run before any statistics commands.
    
-   Sorts grouped statistics in descending order by count.
    

## Installation

1. Clone the repository

```sh
git clone https://github.com/sunilnayakshine/log_analyzer.git
```
2. Ensure Python is installed and install dependencies using:

```sh
pip install pandas

```

## Usage

Run the script with the following commands:

### **Load Data** (Must be run first)

```sh
python main.py --dataload

```

### **Generate Statistics**

-   **By Log Level:**
    
    ```sh
    python main.py --stats-log-level
    
    ```
    
-   **By Service:**
    
    ```sh
    python main.py --stats-service-level
    
    ```
    
-   **By Common Messages:**
    
    ```sh
    python main.py --stats-common-error
    
    ```
    
-   **Fetch Invalid Logs:**
    
    ```sh
    python main.py --invalid-log
    
    ```
    
-   **Run All Statistics:**
    
    ```sh
    python main.py --stats-all
    
    ```
    

## Error Handling

-   If required files are missing, an error is raised:
    
    ```
    exceptions.DataLoadRequiredError: Error: Required files not found. Run --dataload first.
    
    ```
    
-   Ensure that `--dataload` is executed before running any stats commands.
    

## File Outputs

-   `valid_logs.csv` → Contains properly formatted logs.
    
-   `invalid_logs.csv` → Contains malformed log entries.
    

## Example Log Format

```
2024-03-27 12:45:23 - AuthService - ERROR - User authentication failed
2024-03-27 12:46:10 - DBService - INFO - Database connection successful

```
