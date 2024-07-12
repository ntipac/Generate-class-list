# Generate-class-list
The scripts are used to generate an xlsx class list from kolibri activity csv file


# Excel Summary Generator

This Python script generates a summary from multiple Excel files (`.xlsx`). It extracts `class_name`, `centre`, and the total number of learners per `class_name` from each Excel file and saves the summary as both a CSV and an Excel file.

## Requirements

```txt
certifi==2023.7.22
charset-normalizer==3.2.0
et-xmlfile==1.1.0
idna==3.4
numpy==1.25.2
openpyxl==3.1.2
pandas==2.1.0
python-dateutil==2.8.2
pytz==2023.3.post1
requests==2.31.0
six==1.16.0
tzdata==2023.3
urllib3==2.0.4
```
## Usage

```bash
python script.py [-l/--location <excel_files_directory>]
```
