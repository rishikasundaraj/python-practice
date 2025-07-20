import pandas as pd
data = {
    "Fruit": ["Apple", "Banana", "Cherry", "Dates"],
    "Price": [100, 40, 150, 200],
    "Stock": [50, 100, 30, 60]
}

df = pd.DataFrame(data)
print("Fruits stock data:")
print(df)
print("\n Fruit Name:")
print(df["Fruit"])
max_price=df["Price"].max()
most_expensive = df[df["Price"] == max_price]
print("\n Fruit with Highest Price:")
print(most_expensive)
df["Total Value"] = df["Price"] * df["Stock"]
print("\n Updated Data with Total Value:")
print(df)
