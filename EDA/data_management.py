import pandas as pd
import config.js

def load_dataset(file_name):
    data = pd.read_csv(file_name)
    return data

def save_pipeline(pipeline_to_save):