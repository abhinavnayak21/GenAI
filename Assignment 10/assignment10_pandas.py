#Pandas (Series, DataFrame, Functions, Filtering & Analysis)

import pandas as pd


# Task 1: Pandas Series Basics


print("\n--- Task 1: Pandas Series Basics ---")

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

print("Series:")
print(series)

print("\nValues:")
print(series.values)

print("\nIndex:")
print(series.index)

print("\nData Type:")
print(series.dtype)

print("\nFirst Element:")
print(series[0])

print("\nLast Two Elements:")
print(series.tail(2))


# ---------------------------------------------------
# Task 2: Mathematical Operations on Series
# ---------------------------------------------------

print("\n--- Task 2: Mathematical Operations ---")

print("Add 5:")
print(series + 5)

print("\nSubtract 2:")
print(series - 2)

print("\nMultiply by 1.05:")
print(series * 1.05)

print("\nDivide by 2:")
print(series / 2)


# Task 3: Python Functionalities on Series

print("\n--- Task 3: Series Functions ---")

print("Maximum Marks:", series.max())
print("Minimum Marks:", series.min())
print("Sum of Marks:", series.sum())
print("Mean Marks:", series.mean())

# Passed students
passed = series.apply(lambda x: x >= 70)

print("\nPassed Students:")
print(passed)

print("\nNumber of Students Passed:")
print(passed.sum())

# Task 4: Create a DataFrame

print("\n--- Task 4: DataFrame Creation ---")

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("\nDataFrame:")
print(df)

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# Task 5: Important DataFrame Functions

print("\n--- Task 5: DataFrame Functions ---")

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())

print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

# Sort by marks descending
sorted_df = df.sort_values(by='Marks', ascending=False)

# Reset index
sorted_df = sorted_df.reset_index(drop=True)

print("\nSorted DataFrame:")
print(sorted_df)

# Task 6: Filtering & Conditional Selection

print("\n--- Task 6: Filtering ---")

print("\nStudents with marks > 75:")
print(df[df['Marks'] > 75])

print("\nStudents in Math:")
print(df[df['Subject'] == 'Math'])

average_marks = df['Marks'].mean()

print("\nStudents above average:")
print(df[df['Marks'] > average_marks])

print("\nFailed Students (Marks < 70):")
print(df[df['Marks'] < 70])


# Task 7: Grouping & Basic Analysis

print("\n--- Task 7: Grouping & Analysis ---")

print("\nAverage Marks Per Subject:")
print(df.groupby('Subject')['Marks'].mean())

print("\nStudent Count Per Subject:")
print(df.groupby('Subject')['Name'].count())

print("\nMaximum Marks Per Subject:")
print(df.groupby('Subject')['Marks'].max())



# Task 8: Pandas Plotting


print("\n--- Task 8: Plotting ---")

# Bar graph
df.plot(x='Name', y='Marks', kind='bar', title='Student Marks')

# Line graph
df['Marks'].plot(kind='line', title='Marks Line Graph')

# Histogram
df['Marks'].plot(kind='hist', title='Marks Histogram')



# Task 9: Mini Use Case - Sales Data Analysis


print("\n--- Task 9: Sales Data Analysis ---")

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

sales_df = pd.DataFrame(sales)

print("\nSales DataFrame:")
print(sales_df)

print("\nTotal Revenue:")
print(sales_df['Revenue'].sum())

print("\nAverage Daily Revenue:")
print(sales_df['Revenue'].mean())

# Day with highest revenue
max_row = sales_df[sales_df['Revenue'] == sales_df['Revenue'].max()]

print("\nDay with Highest Revenue:")
print(max_row)

# Revenue above average
average_revenue = sales_df['Revenue'].mean()

print("\nDays with Revenue Above Average:")
print(sales_df[sales_df['Revenue'] > average_revenue])

# Plot revenue vs day
sales_df.plot(x='Day', y='Revenue', kind='bar', title='Revenue vs Day')