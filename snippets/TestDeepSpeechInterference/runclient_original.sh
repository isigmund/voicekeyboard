#!/usr/bin/env bash
python3 client_original.py --model ../DeepSpeechModels/deepspeech-0.9.3-models.tflite  \
                           --scorer ../DeepSpeechModels/deepspeech-0.9.3-models.scorer \
                           --audio test1.wav \
                           --extended \
                           --json \
                           --beam_width 500 \
                           --lm_alpha 0.931289039105002 \
                           --lm_beta 1.1834137581510284


