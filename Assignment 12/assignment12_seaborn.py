# Assignment 12: Seaborn Visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

df = pd.read_csv("Student_performance_data _.csv")

print(df.head())

print("\nColumns:")
print(df.columns)


# ---------------------------------------------------
# Task 1: Relational Plot
# ---------------------------------------------------

sns.relplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA",
    hue="Gender"
)

plt.title("Study Time vs GPA")
plt.show()


# Scatter style
sns.relplot(
    data=df,
    x="Absences",
    y="GPA",
    hue="Gender",
    kind="scatter"
)

plt.title("Absences vs GPA")
plt.show()


# ---------------------------------------------------
# Task 2: Line Plot & Faceting
# ---------------------------------------------------

sns.lineplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA"
)

plt.title("Study Time vs GPA")
plt.show()


# Faceting
sns.relplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA",
    col="Gender"
)

plt.show()


# ---------------------------------------------------
# Task 3: Distribution Plots
# ---------------------------------------------------

# Histogram
sns.histplot(df["GPA"])

plt.title("GPA Distribution")
plt.show()


# KDE Plot
sns.kdeplot(df["GPA"])

plt.title("KDE Plot")
plt.show()


# Rug Plot
sns.rugplot(df["GPA"])

plt.title("Rug Plot")
plt.show()


# Histogram + KDE
sns.histplot(df["GPA"], kde=True)

plt.title("Histogram + KDE")
plt.show()


# ---------------------------------------------------
# Task 4: Bivariate Distribution Plots
# ---------------------------------------------------

sns.histplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA"
)

plt.title("Bivariate Histogram")
plt.show()


sns.kdeplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA",
    fill=True
)

plt.title("Bivariate KDE")
plt.show()


# ---------------------------------------------------
# Task 5: Matrix Plots
# ---------------------------------------------------

sns.pairplot(
    df[[
        "StudyTimeWeekly",
        "Absences",
        "GPA"
    ]]
)

plt.show()


# Correlation Heatmap
corr = df[[
    "StudyTimeWeekly",
    "Absences",
    "GPA"
]].corr()

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()


# ---------------------------------------------------
# Task 6: Categorical Plots
# ---------------------------------------------------

# Bar Plot
sns.barplot(
    data=df,
    x="Gender",
    y="GPA"
)

plt.title("Average GPA by Gender")
plt.show()


# Box Plot
sns.boxplot(
    data=df,
    x="ParentalEducation",
    y="GPA"
)

plt.title("Parental Education vs GPA")
plt.show()


# Violin Plot
sns.violinplot(
    data=df,
    x="Gender",
    y="GPA"
)

plt.title("Gender vs GPA")
plt.show()


# Count Plot
sns.countplot(
    data=df,
    x="Gender"
)

plt.title("Gender Count")
plt.show()


# ---------------------------------------------------
# Task 7: Regression Plots
# ---------------------------------------------------

sns.regplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA"
)

plt.title("Regression Plot")
plt.show()


sns.lmplot(
    data=df,
    x="StudyTimeWeekly",
    y="GPA",
    hue="Gender"
)

plt.show()


# ---------------------------------------------------
# Task 8: Multi-Plots & Figure-Level Plots
# ---------------------------------------------------

# FacetGrid
g = sns.FacetGrid(
    df,
    col="Gender"
)

g.map(
    sns.scatterplot,
    "StudyTimeWeekly",
    "GPA"
)

plt.show()


# relplot
sns.relplot(
    data=df,
    x="Absences",
    y="GPA",
    hue="Gender"
)

plt.show()


# catplot
sns.catplot(
    data=df,
    x="Gender",
    y="GPA",
    kind="box"
)

plt.show()


# displot
sns.displot(
    data=df,
    x="GPA",
    kde=True
)

plt.show()