import pandas as pd
import os
import argparse


def process_excel_file(excel_file_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Initialize a dictionary to store class_name counts and associated centres
    class_info = {}

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        class_name = row["class_name"]
        centre = row["centre"]

        # Check if class_name is 0 and set it to "Not assigned"
        if class_name == 0:
            class_name = "Not assigned"

        # Update the class_info dictionary
        if class_name not in class_info:
            class_info[class_name] = {"centre": centre, "total_learners": 0}

        # Increment the total_learners count for the class_name
        class_info[class_name]["total_learners"] += 1

    return class_info


def generate_summary(excel_files_directory, output_location):
    # Initialize an empty list to store the summary information
    summary_data = []

    # Loop through each Excel file in the directory
    for filename in os.listdir(excel_files_directory):
        if filename.endswith(".xlsx"):
            excel_file_path = os.path.join(excel_files_directory, filename)
            class_info = process_excel_file(excel_file_path)

            # Create a summary DataFrame for this Excel file
            summary_df = pd.DataFrame(
                [
                    {
                        "class_name": class_name,
                        "centre": info["centre"],
                        "total_learners": info["total_learners"],
                    }
                    for class_name, info in class_info.items()
                ]
            )

            # Add a column for the filename
            summary_df["filename"] = filename

            # Append this summary DataFrame to the list
            summary_data.append(summary_df)

    # Concatenate all the individual summaries into one DataFrame
    final_summary = pd.concat(summary_data, ignore_index=True)

    # Save the final summary DataFrame to a CSV file
    summary_csv_file = os.path.join(output_location, "summary.csv")
    final_summary.to_csv(summary_csv_file, index=False)

    # Convert the CSV file to an Excel file
    summary_xlsx_file = os.path.join(output_location, "summary.xlsx")
    final_summary.to_excel(summary_xlsx_file, index=False)

    print(f"Summary CSV file saved to {summary_csv_file}")
    print(f"Summary Excel file saved to {summary_xlsx_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a summary from Excel files.")
    parser.add_argument(
        "-l", "--location", type=str, help="Specify the location of Excel files"
    )
    args = parser.parse_args()

    if args.location:
        excel_files_directory = args.location
    else:
        excel_files_directory = os.getcwd()

    generate_summary(excel_files_directory, excel_files_directory)
