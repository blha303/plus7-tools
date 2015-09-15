#!/bin/bash
FN="`./get-last-section.py $1`.mp4"
if [ ! -f $FN ]; then
    echo "Starting on $FN"
    ffmpeg -i `python adammw-plus7/p7-hls.py $1` -acodec copy -vcodec copy -bsf:a aac_adtstoasc $FN
else
    echo "$FN already downloaded"
fi
