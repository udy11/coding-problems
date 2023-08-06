import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 0, parse_dates = True)
df.rename(columns = {'value' : 'views'}, inplace = True)

# Clean data
df = df[(df.loc[:, 'views'] >= df.loc[:, 'views'].quantile(0.025)) & (df.loc[:, 'views'] <= df.loc[:, 'views'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, axs = plt.subplots()
    axs.plot(df, color = 'darkred')
    axs.set_title(r'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axs.set_xlabel('Date')
    axs.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(by = [lambda x : x.strftime('%Y'), lambda x : x.strftime('%B')], sort = False)['views'].mean()
    df_bar.index.rename(names = ('year', 'month'), level = [0, 1], inplace = True)
    df_bar = df_bar.unstack().loc[:, ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')]

    # Draw bar plot
    fig, axs = plt.subplots()
    df_bar.plot(kind = 'bar', xlabel = 'Years', ylabel = 'Average Page Views', ax = axs)
    axs.legend(title = 'Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.loc[:, 'year'] = df_box.index.to_series().apply(lambda x : x.strftime('%Y'))
    df_box.loc[:, 'month'] = df_box.index.to_series().apply(lambda x : x.strftime('%b'))

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2)
    sns.boxplot(x = 'year',  y = 'views', data = df_box, ax = axs[0])
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x = 'month',  y = 'views', data = df_box, ax = axs[1], order = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
