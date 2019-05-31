import pandas

# the top locations that make up targetPercent of the worlds population for the given year
# data taken from the given file (assumed to be the output of the reformated population data)
# populations are in thousands

fileName = "data/TotalPopulation_Medium.csv"
year = "2020"
targetPercent = 0.4  # 0 to 1

popDF = pandas.read_csv(fileName)

# extract the totals per country from the data
yearData = popDF[["Location", "Group", year]]
yearTotals = yearData.loc[yearData["Group"] == "Total"][["Location", year]]  # a DF with the location and its total population for the year given

# extract the world total
worldTotal = yearTotals.loc[yearTotals["Location"] == "World"][year].item()  # get the total world population for the year as given by the data
print(worldTotal)

# remove all non-country locations
### DO BE DONE ###

# find the percent of the world's total by location and add a column with that
yearTotals["Percent"] = yearTotals[year]/worldTotal

# sort by percent of world population
yearTotals.sort_values(by=["Percent"], ascending=False, inplace=True)
# print(yearTotals)

# the locations whos population is greater than targetPercent
# topLocations = yearTotals.loc[yearTotals["Percent"] > targetPercent]
# print(topLocations)

# finds the indexes of the locations that collectively make up targetPercent of the world's population
topIndexes = []
cumsum = 0
for index, series in yearTotals.iterrows():
    cumsum += series[year]
    if cumsum/worldTotal > targetPercent:
        # print(topIndexes)
        break
    topIndexes.append(index)

# create data frame using the indexes from above (top locations using the cumulative sum)
topCumLocations = yearTotals.loc[topIndexes]
print(topCumLocations)
