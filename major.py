#Importing Necessay Python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotply.graph_objs as go
import plotply.express as px
import plotply.io as pio
pio.templates.default = "plotly_white"
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#reading the data
data = pd.read_csv('Netflix Subscriptions.csv')
print(data.head())
