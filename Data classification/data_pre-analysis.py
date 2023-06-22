import pandas as pd
import matplotlib.pyplot as plt

file_path = 'glass+identification/glass.data'
df = pd.read_csv(file_path, header=None)


def count_unique_rows():
    unique_rows = df.drop_duplicates()
    return len(unique_rows)


def plot_count_by_glass_type():
    glass_types = df.iloc[:, -1]
    value_counts = glass_types.value_counts()

    sorted_glass_types = value_counts.index.sort_values()
    sorted_counts = value_counts[sorted_glass_types]

    # Plotting
    plt.figure(figsize=(8, 6))
    sorted_counts.plot(kind='bar')
    plt.xlabel('Glass Type')
    plt.show()


print(f"Number of unique rows in the file: {count_unique_rows()}")
plot_count_by_glass_type()
