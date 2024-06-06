# This shell instruction downloads ts files into one mp4 by referring to the m3u8 source address.
#
# Usage:    ./m3u8.sh <web address of m3u8 with quotation marks> <target mp4 filename>
# Example:  ./m3u8.sh "https://xxx.myqcloud.com/xxxxxx.m3u8" download.mp4

ffmpeg -i $1 $2

# OR

# ffmpeg -i $1 -c copy $2