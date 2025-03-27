import pandas as pd

def stats_by_log_level():
    df = pd.read_csv("valid_logs.csv")
    print(df.groupby(["Log Level"]).size().reset_index(name="Count").to_string(index=False))
    

def stats_by_service():    
    df = pd.read_csv("valid_logs.csv")
    print(df.groupby(["Service"]).size().reset_index(name="Count").to_string(index=False))

    
def stats_by_message():
    df = pd.read_csv("valid_logs.csv")
    print(df.groupby(["Message"]).size().reset_index(name="Count").to_string(index=False))
    
def fetch_invalid_data():
    df = pd.read_csv("invalid_logs.csv")
    print(df)