#!/bin/bash
echo "Verifying tryout folder..."

if [ ! -d "my_folder" ]; then
    echo "Creating folder..." # if folder does not exists
    mkdir "my_folder"
   
else
  echo "Folder exists"  # if folder exists
fi