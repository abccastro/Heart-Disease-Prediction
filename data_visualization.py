
"""
##########################################################################################################################

Data Visualization Methods

This Python file contains a collection of data visualization methods to plot data in a graph like bar graph, boxplot, etc.

Usage:
- Import this file in your Python script.
- Call the desired preprocessing functions with your text data to apply the respective transformation.

##########################################################################################################################
"""

import matplotlib.pyplot as plt
import seaborn as sns


def show_bar_graph(df, col_, figure_size, title, x_label, y_label, x_tick_rotation=None, bar_color=None):
    plt.figure(figsize=figure_size)
    
    if bar_color is not None:
        sns.countplot(x=col_, data=df, palette=bar_color)
    else:
        sns.countplot(x=col_, data=df)
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    if x_tick_rotation is not None:
        plt.xticks(rotation=x_tick_rotation)
    
    plt.show()


def show_boxplot_graph(data, figure_size, title, x_label, box_color="darkblue"):
    """
    Function to plot the boxplot graph
    """
    plt.figure(figsize=figure_size)
    plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor=box_color))
    plt.title(title)
    plt.xlabel(x_label)
    plt.show()