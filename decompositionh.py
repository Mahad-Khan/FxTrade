from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def decompose_plot():
    instrument_name = "AUD_USD"
    data = pd.read_csv("AUD_USD.csv")
    data.set_index('Date')
    series = data["% Rank of DF Avgs"]
    print(series)
    print(type(series))
    result = seasonal_decompose(series, model='additive')
    # result.plot()
    # pyplot.show()
    fig = result.plot()
    title = instrument_name +" Decomposition of Divergence Time series."
    plt.title(title)
    fig_name = "Divergence_Decomposition" + ".png" 
    plt.savefig(fig_name)

decompose_plot()