import pandas as pd

# Introduction to Grouping in pandas
# Hello! In this lesson, we will explore the concept of grouping in pandas. Grouping rows of a DataFrame is a powerful tool that allows you to aggregate rows based on the values in one or more columns of your data. For example, say you have a DataFrame representing all orders in an online store, where each row is an order. You could group the DataFrame by Customer_ID to glean data about particular shoppers. Similarly, if you have a school database where each row corresponds to a student, grouping by Grade_Level can streamline data analysis for each grade. We'll exemplify this operation using a straightforward DataFrame.

# Sample Dataset
# Let's work with a DataFrame of individuals, each characterized by attributes such as Name, Age, and City. Here is a simple example:

df = pd.DataFrame({
    "Name": ["Alex", "Bob", "Chloe", "Charlie", "Alex", "Charlie"],
    "Age": [12, 15, 28, 55, 21, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Los Angeles", "New York", "New York"]
})

# Grouping
# The groupby function in pandas is the basis of group operations. Imagine a pond filled with various types of fish. When different colored foods are dropped into the pond, every fish is drawn to a specific color. After some time, your pond will neatly sort into groups of each type of fish.

# We take the same approach with our DataFrame. Using the pandas groupby method, we will group our data by City. Here's how it's done:

grouped = df.groupby("City")

# Now, the grouped variable is a special pandas DataFrameGroupBy object that has divided our DataFrame into groups by city.

# Exploring DataFrameGroupBy Object
# The DataFrameGroupBy object holds the groups created using groupby. It's like a dictionary: each key is a unique city from our City column, and the corresponding value for each key is a DataFrame comprising all rows with that city in the City column.

# For instance, to view data for "New York" only, pandas offers the get_group function:

print(grouped.get_group("New York"))
'''Output:
      Name  Age      City
0     Alex   12  New York
4     Alex   21  New York
5  Charlie   35  New York
'''

# And there you have it! The function returns a DataFrame containing only the individuals whose City is "New York".

# Applying Aggregation Functions after Grouping
# But we're still going! After dividing our DataFrame into groups, we can perform operations on these groups separately. A typical group operation uses aggregate functions, which take a group of values, calculate, and return a single result. Common examples include taking the sum, average (mean), maximum value (max), or minimum value (min) of a group.

# After grouping, we can calculate the average age of inhabitants for each city:

print(grouped['Age'].mean())
'''Output:
City
Chicago        28.000000
Los Angeles    35.000000
New York       22.666667
'''

# Note how pandas skillfully calculates the mean for each group separately!

# Iterating Through Groups:
# Imagine we want to do something more complex than simply calculate the mean value for each group. In this case, we might want to iterate through all the groups. It is done easily with a regular for loop:

for name, group in grouped:
    print("\nCity:", name)
    print("Number of people:", len(group))
    print("Average age:", group["Age"].mean())
'''Output:
City: Chicago
Number of people: 1
Average age: 28.0

City: Los Angeles
Number of people: 2
Average age: 35.0

City: New York
Number of people: 3
Average age: 22.666666666666668
'''

