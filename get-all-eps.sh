#!/bin/bash
for url in `get-plus7-urls.py $1`
do
    FN="`get-last-section.py $url`.mp4"
    if [ ! -f $FN ]; then
        echo "Starting on $url"
        ffmpeg -i `python adammw-plus7/p7-hls.py $url` -acodec copy -vcodec copy -bsf:a aac_adtstoasc $FN
    else
        echo "$url already downloaded"
    fi
done
