from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns
import os

#Read in the data
path = os.path.relpath("\src\data\messibetis.csv")
df = pd.read_csv(path)