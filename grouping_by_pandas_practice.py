import pandas as pd

population_data = pd.DataFrame({
    "Name": ["Bob", "Alice", "Ashley", "John", "Charlie", "Bob"],
    "City": ["London", "Paris", "Berlin", "London", "Paris", "Berlin"],
    "Age": [45, 36, 42, 29, 53, 31],
    "Income": [55000, 45000, 60000, 37000, 79000, 40000]
})

grouped_data = population_data.groupby("City")
print(grouped_data["Income"].mean())

# Previously, the code printed information about the average age of residents in each city. Now, you must modify the starter code to display the age of the oldest resident in each city.

data = pd.DataFrame({
    "Name": ["Andrew", "Barry", "Chris", "Diane", "Evan", "Fiona"],
    "Age": [24, 30, 36, 42, 48, 54],
    "City": ["Austin", "Boston", "Chicago", "Austin", "Boston", "Chicago"]
})

grouped_data = data.groupby("City")
for city, group in grouped_data:
    print("\nCity:", city)
    print("Number of residents:", len(group))
    print("Oldest resident's age:", group["Age"].max())

data = pd.DataFrame({
    "City": ["London", "London", "New York", "New York", "Tokyo", "Tokyo"],
    "Population": [9000, 8000, 7000, 8500, 9500, 9200],
    "Demographics": ["Youth", "Adults", "Youth", "Adults", "Youth", "Adults"]
})

# TODO: Group data by Demographics
# Please complete the code to calculate the average population, grouping it by Demographics.

grouped_data = data.groupby("Demographics")
print(grouped_data['Population'].mean())

df = pd.DataFrame({
    "City": ["Boston", "Boston", "Chicago", "Phoenix", "Phoenix", "Phoenix"],
    "Population": [1000000, 2000000, 1500000, 3000000, 3500000, 2500000],
    "Year": [1990, 2000, 2010, 1980, 1990, 2000]
})

grouped = df.groupby("City")

for name, group in grouped:
    print("\nCity:", name)
    print("Average Population:", group["Population"].mean())

data = pd.DataFrame({
    "City": ["New York", "Los Angeles", "Chicago", "New York", "Los Angeles", "New York"],
    "District": ["Bronx", "Hollywood", "Westside", "Manhattan", "Burbank", "Staten Island"],
    "Population": [1418207, 1025000, 600000, 1694254, 103341, 476143]
})

# TODO: # Group the DataFrame 'data' by 'City' and calculate the sum of the population
group_data = data.groupby("City")["Population"].sum()

# TODO: Apply for loop to iterate through the grouped DataFrame, and for each group, print the City and the Total Population

# Print the City and the Total Population
for name, population in group_data.items():
    print("\nCity: ", name)
    print("Population: ", population)