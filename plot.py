"""Modul zum Plotten von CSV Daten"""
import pandas as pd
import matplotlib.pyplot as plt


def plot_data() -> None:
    """Funktion zum plotten von runtime.csv mit matplotlib"""
    df = pd.read_csv("runtime.csv")
    plt.plot(df["Durchläufe"], df["Zeit für join_uncorrectly"])
    plt.plot(df["Durchläufe"], df["Zeit für join_correctly"])
    plt.show()
    return


if __name__ == "__main__":
    plot_data()
