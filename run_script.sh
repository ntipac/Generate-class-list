#!/bin/bash

directory="."

rscript="./create_class_list.R"

for file in "$directory"/*.csv; do
    echo "Processing file: $file"

    Rscript "$rscript" "$file"
done
