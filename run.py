"""Modul zum joinen von Strings."""
import measure as measure
import csv
import os


def main():
    """Main function."""
    header = [
        "Durchläufe",
        "Zeit für join_uncorrectly",
        "Zeit für join_correctly",
    ]
    os.remove("runtime.csv")
    with open("runtime.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        data = [0, 0, 0]
        for i in range(100):

            data[0] = i * 10000
            data[1] = measure.join_uncorrectly(i * 10000)
            data[2] = measure.join_correctly(i * 10000)

            writer.writerow(data)


if __name__ == "__main__":
    main()
