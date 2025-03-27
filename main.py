import os
from utilities import process_logs
from arg_parser import arg_parser
from stats import stats_by_log_level, stats_by_message, stats_by_service, fetch_invalid_data


def main():
    arguments = arg_parser()
    
    required_files = ["valid_logs.csv", "invalid_logs.csv"]

    if any([arguments.stats_log_level, arguments.stats_common_message,
            arguments.stats_service_level, arguments.invalid_logs, arguments.stats_all]):
        
        if not all(os.path.exists(file) for file in required_files):
            print("Error: Required files not found. Run --dataload first.")
            return
    
    if arguments.dataload:
        process_logs("app.log")
    if arguments.stats_log_level:
        stats_by_log_level()
    if arguments.stats_common_message:
        stats_by_message()
    if arguments.stats_service_level:
        stats_by_service()
    if arguments.invalid_logs:
        fetch_invalid_data()
    if arguments.stats_all:
        stats_by_log_level()
        stats_by_service()
        stats_by_message()
        

if __name__ == "__main__":
    main()
