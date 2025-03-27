import argparse

def arg_parser():
    parser = argparse.ArgumentParser(
        description="Arguments for Log Analyzer",
        add_help=True,
        epilog="""\
Examples:
  python main.py --dataload                : Cleans the data and saves stats.
  python main.py --stats-all               : Prints all the stats.
  python main.py --stats-log-level         : Prints stats by grouping log level.
  python main.py --stats-service-level     : Prints stats by grouping services.
  python main.py --stats-common-error      : Prints stats by common error messages.
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--dataload",
        action="store_true",
        help="Extract, Clean, and Load the data to files."
    )

    parser.add_argument(
        "--stats-all",
        action="store_true",
        help="Print all the stats"
    )

    parser.add_argument(
        "--stats-log-level",
        dest="stats_log_level",
        action="store_true",
        help="Print stats by grouping log level"
    )

    parser.add_argument(
        "--stats-service-level",
        dest="stats_service_level",
        action="store_true",
        help="Print stats by grouping services"
    )

    parser.add_argument(
        "--stats-common-error",
        dest="stats_common_message",
        action="store_true",
        help="Print stats by common errors"
    )

    parser.add_argument(
        "--invalid-log",
        dest="invalid_logs",
        action="store_true",
        help="Print invalid data"
    )

    return parser.parse_args()
