# help

if [ -z "$1" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ];
then
    echo "Usage: concat.sh [extension] [path]"
    echo "Concatenates all files of the same extension in the specified path into a single file named concat.[extension]"
    echo "If no path is provided, the current directory is used"
    exit 0
fi

# main

ext="$1"
echo: "Target extension: $ext"

if [ -z "$2" ];
then
    echo "No path provided, using current directory."
    path=.
else
    path="$2"
fi

echo "Target path: $path"

cd "$path"
find . -maxdepth 1 -type f -name "*.$ext" | sed "s/.*/file '&'/" | sort | tee concat_list.txt
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy concat.$ext
rm concat_list.txt