#!/bin/sh
while [ "$#" -gt 0 ]; do
    case $1 in
        -i|--input) INPUT="$2"; shift ;;
    esac
    shift
done
ffmpeg -i $INPUT -acodec pcm_s16le -ar 16000 -ac 1 "$INPUT-converted.wav"
/work/src/deinvert -i "$INPUT-converted.wav" "$@"