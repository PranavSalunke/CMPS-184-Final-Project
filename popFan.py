import pandas as pd
# from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt


def createFig(graphMeta, graphData, plot=None):
    variant, country_name, group = graphMeta  # unpack the tuple
    headers, pops = graphData
    if plot is None:
        plot = plt
    # create a new plot with a datetime axis type
    # p = figure(plot_width=800, plot_height=250, title="%s %s %s" % (variant, country_name, group))

    # # make a line graph with the x-axis = header, y = pops, color of the lineis navy, and transparency is 0.5
    # p.line(headers, pops, color='navy', alpha=0.5)
    # p.xaxis.axis_label = "Year"
    # p.yaxis.axis_label = "Population in thousands"

    # show(p)

    plot.scatter(headers, pops)
    return plot


def getPop(variant, country_name, group="Total"):

    filename = "data/TotalPopulation_%s.csv" % (variant)

    cf = pd.read_csv(filename)
    # Get the headers with the years
    headers = list(cf.columns.values)[3:]
    # choose your country
    country = cf.loc[cf["Location"] == country_name]
    # choose the "total" row, extracting the years and making it into a list
    pops = country.loc[country["Group"] == group][headers].values.tolist()[0]
    # from string to float
    pops = list(map(float, pops))

    return (variant, country_name, group), (headers, pops)


variants = ["ConstantFertility", "ConstantMortality", "High", "InstantReplacement", "Low", "Medium", "Momentum", "NoChange", "ZeroMigration"]
# country = "China"
# country = "India"
# country = "United States of America"
country = "Nigeria"


xtix = None
fig, axs = plt.subplots(1, 1)
for v in variants:
    gmeta, gdata = getPop(v, country)
    axs.plot(gdata[0], gdata[1], label=v)

    if xtix is None:
        xtix = [t for t in gdata[0] if int(t) % 5 == 0]


# Shrink current axis by 20%
box = axs.get_position()
axs.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# Put a legend to the right of the current axis
axs.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={"size": 7})

axs.set_xticks(xtix)
plt.title("Population for %s with all variants" % (country))
plt.xticks(rotation=90)
plt.show()
