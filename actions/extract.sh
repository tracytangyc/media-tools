# help
if [ -z "$1" ] || [ "$1" == "--help" ] || [ "$1" == "-h" ];
then
    echo "Usage: extract.sh [input] [start] [end]"
    echo "Extracts a segment from the input file starting and ending at the specified time"
    echo "Time format: HH:MM:SS"
    exit 0
fi

# main
if [ -z "$2" ] || [ -z "$3" ];
then
    echo "Missing start or end time."
    echo "Usage: extract.sh [input] [start] [end]"
    echo "Time format: HH:MM:SS"
    exit 1
fi

sec1=$(date -d "1970-01-01 $2" +%s)
sec2=$(date -d "1970-01-01 $3" +%s)

difference=$((sec2 - sec1))

h=$((difference / 3600))
m=$(((difference % 3600) / 60))
s=$((difference % 3600 % 60))

hhmmss=$(printf "%02d:%02d:%02d\n" $h $m $s)

echo "target duration = $hhmmss"

# input file format: dir/name.ext; output file format: dir/name_extract.ext
out="${1%.*}_extract.${1##*.}"
ffmpeg -i "$1" -ss $2 -t $hhmmss -c copy "$out"
