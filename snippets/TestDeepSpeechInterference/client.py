
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import argparse
import numpy as np
import subprocess
import sys
import wave
import json

from deepspeech import Model, version
from timeit import default_timer as timer


def main():
    parser = argparse.ArgumentParser(description='Running DeepSpeech inference.')
    parser.add_argument('--modelconfig', required=True,
                        help='Path to the model configuration json')
    parser.add_argument('--audio', required=True,
                        help='Path to the audio file to run (WAV format)')
    args = parser.parse_args()

    # load model configuration from json
    with open(args.modelconfig) as f:
      model_config = json.load(f)

    print('Loading model from file {}'.format(model_config['model']), file=sys.stderr)
    ds = Model(model_config['model'])


    if model_config['beam_width']:
        ds.setBeamWidth(model_config['beam_width'])

    desired_sample_rate = ds.sampleRate()

    if model_config['scorer']:
        print('Loading scorer from files {}'.format(model_config['scorer']), file=sys.stderr)
        ds.enableExternalScorer(model_config['scorer'])
        if model_config['lm_alpha'] and model_config['lm_beta']:
            ds.setScorerAlphaBeta(model_config['lm_alpha'], model_config['lm_beta'])

    # check framerate and load audio
    fin = wave.open(args.audio, 'rb')
    fs_orig = fin.getframerate()
    if fs_orig != desired_sample_rate:
        print('Wrong sample rate: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(fs_orig, desired_sample_rate), file=sys.stderr)
        exit()
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1/fs_orig)
    fin.close()


    print('Running inference.', file=sys.stderr)
    inference_start = timer()
    print(ds.stt(audio))
    inference_end = timer() - inference_start
    print('Inference took %0.3fs.' % (inference_end), file=sys.stderr)

if __name__ == '__main__':
    main()
