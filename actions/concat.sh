# (for %i in (*.MP4) do @echo file '%i') > videolist.txt
if [ -z "$1" ]
then
    $path=.
else
    $path=$1
fi

find ${path} -type f -name "*.MP4" -exec echo "file "{} \; > videolist.txt


ffmpeg -f concat -safe 0 -i videolist.txt -c copy output.MP4