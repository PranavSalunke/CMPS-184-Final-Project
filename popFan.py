import pandas as pd
# from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt


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


# variants = ["ConstantFertility", "ConstantMortality", "High", "InstantReplacement", "Low", "Medium", "Momentum", "NoChange", "ZeroMigration"]
variants = ["Low", "Medium", "High"]
# top 61% from 2020

countries = ["China", "United States of America", "Indonesia", "Brazil", "Pakistan",
             "Bangladesh", "Russian Federation", "Mexico", "Japan", "Ethiopia", "Nigeria", "India"]
country = countries[2]

xtix = None
fig, axs = plt.subplots(1, 1)
firstGraphData = None  # used to shade between the first line drawn and last line drawn
lastGraphData = None
for v in variants:
    gmeta, gdata = getPop(v, country)
    axs.plot(gdata[0], gdata[1], label=v)

    lastGraphData = gdata  # set every time
    if firstGraphData is None:
        firstGraphData = gdata  # set only once
    if xtix is None:
        xtix = [t for t in gdata[0] if int(t) % 5 == 0]

# shade between the first line drawn and last line drawn
axs.fill_between(firstGraphData[0], firstGraphData[1], lastGraphData[1], alpha=0.3, color="#e0a05f")

# Shrink current axis by 20%
box = axs.get_position()
axs.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# Put a legend to the right of the current axis
axs.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={"size": 7})

axs.set_xticks(xtix)
plt.title("Population for %s with all variants" % (country))
plt.xticks(rotation=90)
plt.show()
