import pandas as pd
import json
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

with open('imdb_movies_2000to2022.prolific.json', 'r') as f:
    imdb_data = [json.loads(line) for line in f]