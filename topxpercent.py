import pandas
import re
import matplotlib.pyplot as plt

# the top locations that make up targetPercent of the worlds population for the given year
# data taken from the given file (assumed to be the output of the reformated population data)
# populations are in thousands


def graphCumulative(totals):
    plt.xticks(rotation=90)
    plt.plot(totals["Location"], totals["CumPercent"])
    plt.show()


def findTopXPercent(variant, year, targetPercent):
    # returns top Locations as well as cumulative percentage
    fileName = "data/TotalPopulation_%s.csv" % (variant)
    popDF = pandas.read_csv(fileName)

    # extract the totals per country from the data
    yearData = popDF[["LocationID","Location", "Group", year]]
    yearTotals = yearData.loc[yearData["Group"] == "Total"]
    # ^ a DF with the location and its total population for the year given

    # extract the world's total population for the year
    # get the total world population for the year as given by the data
    totalWorldPopulation = yearTotals.loc[yearTotals["Location"] == "World"][year].item()
    # print(totalWorldPopulation)

    with open("country-list.txt") as country_list:
        # read in list of countries
        countries_file = country_list.read()

    # make list of countries
    countries = countries_file.split("\n")  # split on newline instead of whitespace (we want two worded countries)
    countries = [c for c in countries if c]  # remove empty lines
    countriesDF = pandas.DataFrame(data={"countries": countries})
    # print(countriesDF.countries)

    # remove all non-country locations by merging
    # make a common dataframe that has only countries and removes non-countries, dropping na values
    common = countriesDF.merge(yearTotals, how='inner', left_on=['countries'], right_on=['Location'])
    yearTotals = common.dropna()
    yearTotals = yearTotals.drop(columns=["countries"])  # drop countries since same as location
    # print(yearTotals)

    # find the percent of the world's total by location and add a column with that
    yearTotals["Percent"] = yearTotals[year]/totalWorldPopulation  # % of the world's population

    # sort by percent of world population
    yearTotals.sort_values(by=["Percent"], ascending=False, inplace=True)
    # print(yearTotals)

    # find the cumulative sum of percent
    yearTotals["CumPercent"] = yearTotals["Percent"].cumsum()
    # print(yearTotals)

    # find the locations that collectively make up targetPercent of the world's population
    topLocations = yearTotals[yearTotals["CumPercent"] < targetPercent]
    print(topLocations)

    # the locations with populations than targetPercent (not needed, but done for fun)
    # greaterLocations = yearTotals.loc[yearTotals["Percent"] > targetPercent]
    # print(greaterLocations)

    return yearTotals, topLocations


variant = "Medium"  # can be:
#  "ConstantFertility" "ConstantMortality" "High" "InstantReplacement" "Low" "Medium" "Momentum" "NoChange" "ZeroMigration"

year = "2020"
targetPercent = 0.61  # 0 to 1

# returns top Locations as well as cumulative percentage
cumulativeTotals, topLocations = findTopXPercent(variant, year, targetPercent)

# graph the cumulative sum (does not depend on targetPercent)
# graphCumulative(cumulativeTotals)
graphCumulative(topLocations)  # plot only the topLocations
