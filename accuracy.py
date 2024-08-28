import os
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

def save_plot(fig, filename):
    folder = "Conclusion"
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, filename)
    fig.savefig(file_path)
    print(f"Saved plot to {file_path}")

def calculate_accuracy(csv_file="Data/gender_analysis.csv"):
    df = pd.read_csv(csv_file)
    
    df.columns = df.columns.str.strip()

    if 'Actual Gender' not in df.columns or 'Dominant Gender' not in df.columns:
        print("Error: 'Actual Gender' or 'Dominant Gender' column not found in CSV file.")
        print("Available columns:", df.columns.tolist())
        return
    
    y_true = df['Actual Gender']
    y_pred = df['Dominant Gender']

    accuracy = accuracy_score(y_true, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")

    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(conf_matrix)

    report = classification_report(y_true, y_pred)
    print("Classification Report:")
    print(report)

    fig1 = plt.figure(figsize=(6, 6))
    plt.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.5, fignum=0)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            plt.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center')

    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')
    save_plot(fig1, "confusion_matrix.png")

    fig2 = plt.figure(figsize=(6, 6))
    plt.bar(['Model Accuracy'], [accuracy * 100], color='blue')
    plt.ylim(0, 100)
    plt.ylabel('Accuracy (%)')
    plt.title('Model Accuracy')
    save_plot(fig2, "model_accuracy.png")

if __name__ == "__main__":
    calculate_accuracy()
