

import pandas as pd

# Read the CSV file
df = pd.read_csv(r"/Users/restaff/Downloads/lisbon.csv")

# Convert date_time to datetime format
df['date_time'] = pd.to_datetime(df['date_time'], format='%Y-%m-%d')

# Add year column for easier analysis
df['year'] = df['date_time'].dt.year

# View the first few rows and data info
print("First 5 rows of our data:")
print(df.head())

# Check the data types of our columns
print("\nData types of each column:")
print(df.dtypes)

# Quick summary of our numeric columns
print("\nSummary statistics:")
print(df.describe())

# Calculate average temperature by year
yearly_avg_temp = df.groupby('year')['tempC'].mean()
print("\nYearly Average Temperatures:")
print(yearly_avg_temp.round(1))

# Find the warmest and coldest years
warmest_year = yearly_avg_temp.idxmax()
coldest_year = yearly_avg_temp.idxmin()
print(f"\nWarmest year was {warmest_year} with average temperature: {yearly_avg_temp[warmest_year]:.1f}°C")
print(f"Coldest year was {coldest_year} with average temperature: {yearly_avg_temp[coldest_year]:.1f}°C")

# Calculate yearly temperature ranges
yearly_stats = df.groupby('year').agg({
    'tempC': ['mean', 'min', 'max'],
    'humidity': 'mean',
    'precipMM': 'sum'
}).round(1)

print("\nYearly Statistics:")
print(yearly_stats)



#part 3
hot_days = df[df['maxtempC'] > 35].groupby('year').size()
average_wind_speed = df.groupby('speed').mean()

