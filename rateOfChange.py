import pandas as pd
from numpy import diff
import matplotlib.pyplot as plt
import generalGifs


def getPop(variant, country_name, group="Total"):

    filename = "data/TotalPopulation_%s.csv" % (variant)

    cf = pd.read_csv(filename)
    # Get the headers with the years
    years = list(cf.columns.values)[4:]
    # choose your country
    country = cf.loc[cf["Location"] == country_name]
    # choose the "total" row, extracting the years and making it into a list
    pop = country.loc[country["Group"] == group][years].values.tolist()[0]
    # from string to float
    pop = list(map(float, pop))
    years = list(map(int, years))

    return (variant, country_name, group), (years, pop)


def saveGraph(filename, data, meta):
    variant, country, group = meta
    pop, first, second, years = data

    plt.xticks(rotation=90)
    plt.title("%s | %s, %s" % (variant, group, country))
    plt.plot(years[1:], first, label='first')
    plt.plot(years[2:], second, label='second')
    plt.plot(years, [0]*len(years), color="black", linestyle='dashed', linewidth="0.5", label="zero")
    plt.legend()
    plt.savefig(filename, bbox_inches='tight')
    plt.clf()


variants = ["ConstantFertility", "ConstantMortality", "High", "InstantReplacement", "Low", "Medium", "Momentum", "NoChange", "ZeroMigration"]

country = "China"
group = "Total"
generalGifs.initFolders()
imageNames = []
for var in variants:
    meta, (years, pop) = getPop(var, country, group)

    # get first derivative
    first = diff(pop)
    # get second derivative
    second = diff(first)
    filename = "tempimages/%s_%s_%s.png" % (group, country, var)
    imageNames.append(filename)
    saveGraph(filename, (pop, first, second, years), meta)

generalGifs.createGif(imageNames, "rateOfChange_%s_%s.gif" % (country, group), 1)