#!/bin/bash

WATCH_FOLDER=${WATCH_FOLDER:-"./files"} 

mkdir -p "${WATCH_FOLDER}"  

# Monitor the specified folder for any new json files
inotifywait -m "${WATCH_FOLDER}" -e create -e moved_to | while read path action file; do
    echo "New file detected: $file"
    
    if [[ "$file" == *.json ]] && [[ ! "$file" == Response_* ]]; then
        python3 createResponse.py "$WATCH_FOLDER/$file"
    fi
done