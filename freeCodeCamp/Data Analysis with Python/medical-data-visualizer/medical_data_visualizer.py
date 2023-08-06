import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df.loc[:, 'overweight'] = (1.0e4 * df.loc[:, 'weight'] / (df.loc[:, 'height']**2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[:, 'cholesterol'] = (df.loc[:, 'cholesterol'] > 1).astype(int)
df.loc[:, 'gluc'] = (df.loc[:, 'gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data = df_cat, x = 'variable', col = 'cardio', kind = 'count', hue = 'value')
    fig.set_ylabels('total')

    # Get the figure for the output
    fig = fig.fig
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    dfap = df.loc[:, 'ap_lo'] <= df.loc[:, 'ap_hi']
    dfh0 = df.loc[:, 'height'] >= df.loc[:, 'height'].quantile(0.025)
    dfh1 = df.loc[:, 'height'] <= df.loc[:, 'height'].quantile(0.975)
    dfw0 = df.loc[:, 'weight'] >= df.loc[:, 'weight'].quantile(0.025)
    dfw1 = df.loc[:, 'weight'] <= df.loc[:, 'weight'].quantile(0.975)
    df_heat = df[dfap & dfh0 & dfh1 & dfw0 & dfw1]

    # Calculate the correlation matrix
    corr = np.corrcoef(df_heat.to_numpy().transpose())

    # Generate a mask for the upper triangle
    mask = np.array([[j >= i for j in range(corr.shape[1])] for i in range(corr.shape[0])])
    corr[mask] = None

    # Set up the matplotlib figure
    fig, axs = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, ax = axs, annot = True, fmt = '.1f', xticklabels = df_heat.columns, yticklabels = df_heat.columns, center = 0.1, square = True, linewidth = 0.1, linecolor = 'white')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
