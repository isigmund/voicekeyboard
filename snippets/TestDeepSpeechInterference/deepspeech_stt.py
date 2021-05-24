
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



class SttException(Exception):
    def __init__(self, message='General Exception'):
        # Call the base class constructor with the parameters it needs
        super(SttException, self).__init__(message)



def initialize_stt(model_config):
    ds = Model(model_config['model'])

    if model_config['beam_width']:
        ds.setBeamWidth(model_config['beam_width'])

    desired_sample_rate = ds.sampleRate()

    if model_config['scorer']:
        ds.enableExternalScorer(model_config['scorer'])
        if model_config['lm_alpha'] and model_config['lm_beta']:
            ds.setScorerAlphaBeta(model_config['lm_alpha'], model_config['lm_beta'])

    return ds, desired_sample_rate


def get_audio(filename, desired_sample_rate):
    # check framerate and load audio
    fin = wave.open(filename, 'rb')
    fs_orig = fin.getframerate()
    if fs_orig != desired_sample_rate:
        raise SttException('Wrong sample rate: original sample rate ({}) is different than {}hz.'.format(fs_orig, desired_sample_rate))
        exit()
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
    fin.close()
    return audio


def get_text_from_audio(ds, desired_sample_rate, filename):
    audio = get_audio(filename, desired_sample_rate)
    return ds.stt(audio)



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

    try:
      ds, desired_sample_rate = initialize_stt(model_config)
      text = get_text_from_audio(ds, desired_sample_rate, args.audio)
      print(text)
    except SttException as e:

      print(e)


if __name__ == '__main__':
    main()
