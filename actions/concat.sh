(for %i in (*.MP4) do @echo file '%i') > videolist.txt

ffmpeg -f concat -safe 0 -i videolist.txt -c copy output.MP4