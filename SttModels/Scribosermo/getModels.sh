#!/usr/bin/env bash


# english model from https://gitlab.com/Jaco-Assistant/Scribosermo
wget -O scribosermo_en_model_full.tflite https://download1349.mediafire.com/90i4619hgacg/7q17n5ornb80ygo/model_full.tflite
wget -O scribosermo_en.scorer https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

#german model from https://gitlab.com/Jaco-Assistant/Scribosermo  does not work
wget -O scribosermo_de_model_full.tflite https://download1647.mediafire.com/fasti1es5lhg/ti0tz35ajn7zbrb/model_full.tflite
wget -O scribosermo_de.scorer https://download1076.mediafire.com/xugomyseippg/pzj8prgv2h0c8ue/kenlm_de_all.scorer

