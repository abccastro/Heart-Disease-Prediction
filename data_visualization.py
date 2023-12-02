
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


def show_bar_graph(df, col_, figure_size, title, x_label, y_label, x_tick_rotation, bar_color=['darkblue']):
    """
    Function to plot the bar graph
    """
    # Extract the data for plotting
    value_count_df = df.groupBy(col_).count().orderBy(col_)
    values = value_count_df.select(col_).rdd.flatMap(lambda x: x).collect()
    count_values = value_count_df.select("count").rdd.flatMap(lambda x: x).collect()

    # Plotting the bar graph
    plt.figure(figsize=figure_size)
    plt.bar(values, count_values, color=bar_color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    if x_tick_rotation is not None:
        plt.xticks(rotation=x_tick_rotation, ha='right')
    
    plt.title(title)
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