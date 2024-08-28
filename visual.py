import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(csv_file="Data/gender_analysis.csv"):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Count the occurrences of each dominant gender
    gender_counts = df['Dominant Gender'].value_counts()

    # Create a bar chart
    plt.figure(figsize=(8, 6))
    gender_counts.plot(kind='bar', color=['blue', 'pink'])
    plt.title('Dominant Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    visualize_data()