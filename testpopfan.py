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
country = "United States of America"
for v in variants:
   gmeta, gdata = getPop(v, country)
   plt.plot(gdata[0],gdata[1],label=v)

#gmeta, gdata = getPop("Medium", country)
#p = createFig(gmeta, gdata)
#p.show()
#plt.plot(gdata[0],gdata[1], label="M")
gmeta, gdata = getPop("High", country)
#p = createFig(gmeta, gdata, p)
#p.show()
#plt.plot(gdata[0],gdata[1],label="H")

#gmeta, gdata = getPop("NoChange", country)
#plt.plot(gdata[0],gdata[1],label="N")
plt.legend()
plt.show()