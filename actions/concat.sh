# (for %i in (*.MP4) do @echo file '%i') > videolist.txt
if [ -z "$1" ]
then
    $path=.
else
    $path=$1
fi

find ${path} -maxdepth 1 -type f -name "*.MP4" | sed 's/.*/file &/' | sort | tee videolist.txt
cat videolist.txt
ffmpeg -f concat -safe 0 -i videolist.txt -c copy -acodec copy output.MP4
rm videolist.txt