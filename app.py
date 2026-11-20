# ==========================================
# CAMPUS ELECTRICITY ANALYZER
# Python Data Analytics Project
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. Read Dataset
data = pd.read_csv("electricity_data.csv")

print("\n================================")
print("     CAMPUS ELECTRICITY ANALYZER")
print("================================")

# 2. Display Complete Dataset
print("\n1. ELECTRICITY DATA")
print(data.to_string(index=False))

# 3. Calculate Electricity Bill
data["Bill"] = data["Units"] * data["Rate"]

# 4. Total Electricity Consumption
total_units = data["Units"].sum()

print("\n2. TOTAL ELECTRICITY CONSUMPTION")
print("Total Units:", total_units, "kWh")

# 5. Total Electricity Bill
total_bill = data["Bill"].sum()

print("\n3. TOTAL ELECTRICITY BILL")
print("Total Bill: Rs.", total_bill)

# 6. Building-wise Analysis
building_usage = data.groupby("Building")["Units"].sum()

print("\n4. BUILDING-WISE ELECTRICITY USAGE")
print(building_usage)

highest_building = building_usage.idxmax()
highest_units = building_usage.max()

print("\n5. HIGHEST ELECTRICITY CONSUMPTION")
print("Building:", highest_building)
print("Units:", highest_units, "kWh")

# 8. Find Lowest Electricity Consuming Building
lowest_building = building_usage.idxmin()
lowest_units = building_usage.min()

print("\n6. LOWEST ELECTRICITY CONSUMPTION")
print("Building:", lowest_building)
print("Units:", lowest_units, "kWh")

# 9. Average Electricity Consumption
average_units = building_usage.mean()

print("\n7. AVERAGE ELECTRICITY CONSUMPTION")
print("Average:", round(average_units, 2), "kWh")

# 10. Monthly Electricity Analysis
monthly_usage = data.groupby("Month")["Units"].sum()

print("\n8. MONTHLY ELECTRICITY CONSUMPTION")
print(monthly_usage)

# 11. Data Structure - Dictionary
electricity_dictionary = building_usage.to_dict()

print("\n9. ELECTRICITY DATA IN DICTIONARY")
print(electricity_dictionary)

# 12. Data Structure - List
building_list = list(building_usage.index)

print("\n10. BUILDING LIST")
print(building_list)

# 13. Data Structure - Set
unique_buildings = set(building_list)

print("\n11. UNIQUE BUILDINGS")
print(unique_buildings)

# 14. Electricity Saving Suggestions
print("\n12. ELECTRICITY SAVING SUGGESTIONS")

for building, units in building_usage.items():

    if units > average_units:
        print(building, "has high consumption.")
        print("Suggestion: Switch off unused lights and equipment.")

    else:
        print(building, "has comparatively lower consumption.")

# 15. Bar Chart - Building Wise Consumption
plt.figure(figsize=(9, 5))

building_usage.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Building Wise Electricity Consumption")
plt.xlabel("Campus Buildings")
plt.ylabel("Electricity Units (kWh)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("building_consumption.png")
plt.show()

# 16. Pie Chart - Electricity Distribution
plt.figure(figsize=(7, 7))

building_usage.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Campus Electricity Consumption Distribution")
plt.ylabel("")

plt.savefig("electricity_distribution.png")
plt.show()

# 17. Monthly Consumption Graph
plt.figure(figsize=(8, 5))

monthly_usage.plot(
    kind="line",
    marker="o",
    color="green"
)

plt.title("Monthly Electricity Consumption")
plt.xlabel("Month")
plt.ylabel("Electricity Units (kWh)")
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_consumption.png")
plt.show()

# 18. Save Analyzed Data
data.to_csv("analyzed_electricity_data.csv", index=False)

print("\n================================")
print("PROJECT EXECUTION COMPLETED!")
print("================================")
print("Analyzed data saved successfully.")
print("Graphs saved successfully.")