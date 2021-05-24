#!/usr/bin/env bash

#english models from deepspeech 0.9.3 release
wget -O deepspeech_en_0.9.3_model.tflite https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.tflite
wget -O deepspeech_en_0.9.3_model.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

# german modfel from DeepSpeech-PolyGlot-DE  https://drive.google.com/drive/folders/1oO-N-VH_0P89fcRKWEUlVDm-_z18Kbkb
./getGoogleDriveFile.sh 1CMnImO3ucu3j0q63OqoBIyW-09dHUE4p deepspeech_polyglot_de_kenlm_de.scorer
./getGoogleDriveFile.sh 1Chx2n4u8PXTBwxAmDGGem9PKcd8sBhbQ deepspeech_polyglot_de_output_graph_de.tflite

