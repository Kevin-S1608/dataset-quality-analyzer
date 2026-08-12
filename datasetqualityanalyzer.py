import pandas as pd
import numpy as np

print("=" * 60)
print("              DATASET QUALITY ANALYZER")
print("=" * 60)

file_path = input("Enter the CSV file path: ")

try:
    data = pd.read_csv(file_path)

    print("\nDataset loaded successfully!")

    # -----------------------------
    # BASIC DATASET INFORMATION
    # -----------------------------

    rows = data.shape[0]
    columns = data.shape[1]

    numeric_columns = data.select_dtypes(include=np.number).columns
    text_columns = data.select_dtypes(include=["str"]).columns

    # -----------------------------
    # MISSING VALUES
    # -----------------------------

    missing_values = data.isnull().sum()
    total_missing = missing_values.sum()

    # -----------------------------
    # DUPLICATES
    # -----------------------------

    duplicate_count = data.duplicated().sum()

    # -----------------------------
    # OUTLIERS
    # -----------------------------

    total_outliers = 0

    for column in numeric_columns:

        values = data[column].dropna()

        if len(values) < 4:
            continue

        Q1 = values.quantile(0.25)
        Q3 = values.quantile(0.75)

        IQR = Q3 - Q1

        lower_limit = Q1 - 1.5 * IQR
        upper_limit = Q3 + 1.5 * IQR

        outliers = values[
            (values < lower_limit) |
            (values > upper_limit)
        ]

        total_outliers += len(outliers)

    # -----------------------------
    # QUALITY SCORE
    # -----------------------------

    score = 100

    if rows > 0 and columns > 0:
        missing_percentage = (
            total_missing / (rows * columns)
        ) * 100

        missing_penalty = min(missing_percentage, 30)

    else:
        missing_penalty = 0

    if rows > 0:
        duplicate_percentage = (
            duplicate_count / rows
        ) * 100

        duplicate_penalty = min(duplicate_percentage, 20)

    else:
        duplicate_penalty = 0

    if rows > 0:
        outlier_percentage = (
            total_outliers / rows
        ) * 100

        outlier_penalty = min(outlier_percentage, 20)

    else:
        outlier_penalty = 0

    score = score - (
        missing_penalty
        + duplicate_penalty
        + outlier_penalty
    )

    score = max(0, round(score, 2))

    # -----------------------------
    # QUALITY CLASSIFICATION
    # -----------------------------

    if score >= 90:
        quality = "Excellent"

    elif score >= 75:
        quality = "Good"

    elif score >= 50:
        quality = "Needs Improvement"

    else:
        quality = "Poor"

    # -----------------------------
    # RECOMMENDATIONS
    # -----------------------------

    recommendations = []

    if total_missing > 0:
        recommendations.append(
            "Review and handle missing values."
        )

    if duplicate_count > 0:
        recommendations.append(
            "Review and remove unnecessary duplicate records."
        )

    if total_outliers > 0:
        recommendations.append(
            "Review potential outliers before performing analysis."
        )

    if (
        total_missing == 0
        and duplicate_count == 0
        and total_outliers == 0
    ):
        recommendations.append(
            "No major quality issues detected."
        )

    # -----------------------------
    # FINAL PROFESSIONAL REPORT
    # -----------------------------

    print("\n")
    print("=" * 60)
    print("                 DATASET QUALITY REPORT")
    print("=" * 60)

    print("\nDataset:")
    print(" ", file_path)

    print("\n--- DATASET OVERVIEW ---")
    print("Rows                    :", rows)
    print("Columns                 :", columns)
    print("Numeric Columns         :", len(numeric_columns))
    print("Text Columns            :", len(text_columns))

    print("\n--- QUALITY ANALYSIS ---")
    print("Missing Values          :", total_missing)
    print("Duplicate Rows          :", duplicate_count)
    print("Potential Outliers      :", total_outliers)

    print("\n--- QUALITY SCORE ---")
    print("Missing Value Penalty   :", round(missing_penalty, 2))
    print("Duplicate Penalty       :", round(duplicate_penalty, 2))
    print("Outlier Penalty         :", round(outlier_penalty, 2))

    print("\nQUALITY SCORE            :", score, "/ 100")
    print("QUALITY LEVEL            :", quality)

    print("\n--- RECOMMENDATIONS ---")

    for number, recommendation in enumerate(
        recommendations, start=1
    ):
        print(str(number) + ".", recommendation)

    print("\n" + "=" * 60)
    print("             ANALYSIS COMPLETED")
    print("=" * 60)

except FileNotFoundError:
    print("\nFile not found. Check the CSV file path.")

except Exception as e:
    print("\nError:", e)
