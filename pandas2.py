import pandas as pd
df = pd.read_csv(r"C:\Users\rishi\OneDrive\Documents\inventory.csv")
data = {
    'Item': ['Laptop', 'Headphones', 'T-shirt', 'Jeans', 'Apples', 'Milk'],
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Grocery', 'Grocery'],
    'Price': [70000, 1500, 500, 1200, 100, 60],
    'Stock': [10, 50, 200, 80, 150, 0]
}

df = pd.DataFrame(data)
print(df)
df.to_csv("inventory.csv", index=False)
print("CSV file created successfully!")
