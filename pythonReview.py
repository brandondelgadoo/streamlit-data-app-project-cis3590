import pandas as pd

water_data = {
    "temperature": [67, 69, 71],
    "pH": [6.7, 6.5, 6.9],
    "oxygen": [7.1, 5.6, 4.2]
}

df = pd.DataFrame(water_data)
print(df)