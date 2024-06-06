sec1=$(date -d "1970-01-01 $2" +%s)
sec2=$(date -d "1970-01-01 $3" +%s)

difference=$((sec2 - sec1))

h=$((difference / 3600))
m=$(((difference % 3600) / 60))
s=$((difference % 3600 % 60))

hhmmss=$(printf "%02d:%02d:%02d\n" $h $m $s)

echo target duration = $hhmmss

ffmpeg -i $1 -ss $2 -t $hhmmss -acodec copy "crop $1"