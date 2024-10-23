#!/bin/bash

# Check if the folder name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <target_folder>"
    exit 1
fi

TARGET_FOLDER="$1"
TEMPLATE_FOLDER="template"

# Create the target folder if it doesn't exist
if [ ! -d "$TARGET_FOLDER" ]; then
    echo "Creating target folder: $TARGET_FOLDER"
    mkdir -p "$TARGET_FOLDER"
fi

# Move solution.py and testcases.txt from the current directory to the target folder
for file in solution.py testcases.txt; do
    if [ -e "$file" ]; then
        echo "Moving $file to $TARGET_FOLDER"
        mv "$file" "$TARGET_FOLDER"
    else
        echo "$file does not exist in the current directory."
    fi
done

# Copy solution.py and testcases.txt from the template folder to the current working directory
for file in solution.py testcases.txt; do
    SOURCE_FILE="$TEMPLATE_FOLDER/$file"
    if [ -e "$SOURCE_FILE" ]; then
        echo "Copying $SOURCE_FILE to the current working directory"
        cp "$SOURCE_FILE" .
    else
        echo "$SOURCE_FILE does not exist in the template folder."
    fi
done

echo "Operation completed."


# Output file path
output_file="num_solved_problems.txt"

# Count directories with names that are numbers
count=0

# Loop through all directories in the current folder
for dir in */ ; do
    # Check if the directory name is a number (using regular expression)
    if [[ ${dir%/} =~ ^[0-9]+$ ]]; then
        ((count++))
    fi
done

# Write the count to the output file, overwriting if it already exists
echo "$count" > "$output_file"

echo "Count has been written to $output_file"