# Assignment 11: Matplotlib (Core Plot Types & Visualization)

import matplotlib.pyplot as plt


# Task 1: Line Plot (Sales Trend)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1800, 1700, 2000, 2200]

plt.figure()
plt.plot(months, sales)

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

# Task 2: Scatter Plot

study_hours = [1, 2, 3, 4, 5, 6]
marks = [50, 55, 65, 70, 80, 90]

plt.figure()
plt.scatter(study_hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# Task 3: Bar Plot

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
sales_values = [50, 120, 80, 40]

# Vertical bar chart
plt.figure()
plt.bar(products, sales_values)

plt.title("Product Sales (Vertical)")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

# Horizontal bar chart
plt.figure()
plt.barh(products, sales_values)

plt.title("Product Sales (Horizontal)")
plt.xlabel("Sales")
plt.ylabel("Products")

plt.show()

# Task 4: Multiple Bar Plot

years = ["2022", "2023", "2024"]

sales_a = [100, 120, 140]
sales_b = [90, 110, 130]

x = range(len(years))
width = 0.4

plt.figure()

plt.bar(x, sales_a, width=width, label="Store A")
plt.bar([i + width for i in x], sales_b, width=width, label="Store B")

plt.title("Sales Comparison")
plt.xlabel("Years")
plt.ylabel("Sales")

plt.xticks([i + width / 2 for i in x], years)

plt.legend()

plt.show()


# Task 5: Stacked Bar Chart

boys = [40, 35, 30]
girls = [30, 25, 20]

subjects = ["Math", "Science", "English"]

plt.figure()

plt.bar(subjects, boys, label="Boys")
plt.bar(subjects, girls, bottom=boys, label="Girls")

plt.title("Students per Subject")
plt.xlabel("Subjects")
plt.ylabel("Count")

plt.legend()

plt.show()

# Task 6: Histogram

marks_data = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.figure()

plt.hist(marks_data, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()


# Task 7: Pie Chart

categories = ["Electronics", "Clothing", "Food", "Books"]
market_share = [40, 25, 20, 15]

plt.figure()

plt.pie(
    market_share,
    labels=categories,
    autopct='%1.1f%%'
)

plt.title("Market Share")

plt.show()