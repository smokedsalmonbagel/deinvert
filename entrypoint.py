#!/bin/python
import subprocess
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Deinvert scrambled audio recordings.')
parser.add_argument('-f','--frequency', help='Frequency of the inversion carrier, in Hertz.', required=False)
parser.add_argument('-i','--input-file', help='Use an audio file as input. All formats supported by libsndfile should work.', required=True)
parser.add_argument('-o','--output-file', help='Write output to a WAV file instead of stdout. An existing file will be overwritten.', required=True)
parser.add_argument('-p','--preset', help='Scrambler frequency preset (1-8), referring to the set of common carrier frequencies used by e.g. the Selectone ST-20B scrambler.', required=False)
parser.add_argument('-q','--quality', help='Filter quality, from 0 (worst quality, low CPU usage) to 3 (best quality, higher CPU usage). The default is 2.', required=False)
parser.add_argument('-r','--samplerate', help='Sampling rate of raw input audio, in Hertz.', required=False)
parser.add_argument('-s','--split-frequency', help='Split point for split-band inversion, in Hertz.', required=False)
parser.add_argument('-v','--version', help='Display version string.', required=False)
args = vars(parser.parse_args())
print(args)

ext = Path(args['input_file']).suffix
stem = Path(args['input_file']).stem # input
temp_path = 'temp.wav'


cmd = ['ffmpeg', '-i', args['input_file'], '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', temp_path]
subprocess.call(cmd)

arglist = ['/work/src/deinvert']
for key, val in args.items():
    if val is not None:
        argname = key.replace('_','-')
        arglist.append('--'+argname)
        if key == 'input_file':
            arglist.append(temp_path)
        else:
            arglist.append(val)
print(arglist)
subprocess.call(arglist)