import requests

# Download the Abalone dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
response = requests.get(url)
with open("abalone.data", "wb") as file:
    file.write(response.content)
    
# to read
# import pandas as pd
# df = pd.read_csv("abalone.data", header=None)