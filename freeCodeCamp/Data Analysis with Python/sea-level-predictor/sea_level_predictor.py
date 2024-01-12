import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    year_last = 2050
    year_1 = 2000
    years_0 = np.arange(df.loc[0, 'Year'], year_last + 1, 1)
    years_1 = np.arange(year_1, year_last + 1, 1)

    # Create scatter plot
    plt.scatter(df.loc[:, 'Year'], df.loc[:, 'CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    m0, c0, _, _, _ = linregress(df.loc[:, 'Year'], df.loc[:, 'CSIRO Adjusted Sea Level'])
    plt.plot(years_0, m0 * years_0 + c0, color = 'orange')

    # Create second line of best fit
    df1 = df.loc[:, ('Year', 'CSIRO Adjusted Sea Level')][df.loc[:, 'Year'] >= year_1]
    m1, c1, _, _, _ = linregress(df1.loc[:, 'Year'], df1.loc[:, 'CSIRO Adjusted Sea Level'])
    plt.plot(years_1, m1 * years_1 + c1, color = 'red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
