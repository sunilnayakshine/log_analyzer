import pandas as pd

def stats_by_log_level():
    """
    Groups valids by log level.
    Args: None
    Return: None
    """
    df = pd.read_csv("valid_logs.csv")
    print(df.groupby(["Log Level"]).size().reset_index(name="Count").to_string(index=False))
    

def stats_by_service():  
    """
    Groups valids by Services.
    Args: None
    Return: None
    """  
    df = pd.read_csv("valid_logs.csv")
    print(df.groupby(["Service"]).size().reset_index(name="Count").to_string(index=False))

    
def stats_by_message():
    """
    Groups valids by messages.
    Args: None
    Return: None
    """
    df = pd.read_csv("valid_logs.csv")
    print(df.groupby(["Message"]).size().reset_index(name="Count").to_string(index=False))
    
def fetch_invalid_data():
    """
    Perints the invalid logs.
    Args: None
    Return: None
    """
    df = pd.read_csv("invalid_logs.csv")
    print(df)