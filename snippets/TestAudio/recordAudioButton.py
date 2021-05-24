from time import sleep
import pyaudio
import wave
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

button_pin = 10

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 16000  # 16kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 1 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file


audio = pyaudio.PyAudio() # create pyaudio instantiation



def setup():
    # setip GPIO
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    # set up the edge detection
    GPIO.add_event_detect(button_pin, GPIO.BOTH, bouncetime=500)


def main():
    frames  = []
    recording_active = False

    try:
        while True:
            if recording_active == True:
                data = stream.read(chunk)
                frames.append(data)

            if GPIO.event_detected(button_pin):
                # if we're here, an edge was recognized
                sleep(0.005) # debounce for 5mSec
                # only show valid edges
                if GPIO.input(button_pin) == 1:
                    print ("Start recording")
                    recording_active =  True

		    # create pyaudio stream
                    stream = audio.open(format = form_1,
                                        rate = samp_rate,
                                        channels = chans,
                                        input_device_index = dev_index,
                                        input = True,
                                        frames_per_buffer=chunk)

                else:
                    print ("End recording")
                    recording_active = False

                    # stop the stream, close it, and terminate the pyaudio instantiation
                    stream.stop_stream()
                    stream.close()

                    # save the audio frames as .wav file
                    wavefile = wave.open(wav_output_filename,'wb')
                    wavefile.setnchannels(chans)
                    wavefile.setsampwidth(audio.get_sample_size(form_1))
                    wavefile.setframerate(samp_rate)
                    wavefile.writeframes(b''.join(frames))
                    wavefile.close()
                    frames = []

    except KeyboardInterrupt:
        pass
    finally:
        print ("\nRelease the used pin(s) and terminate audio")
        GPIO.cleanup([button_pin])
        audio.terminate()




if __name__ == '__main__':
    setup()
    main()























###GPIO.add_event_detect(button_pin,GPIO.BOTH,callback=my_callback, bouncetime=500) # Setup event on pin 10 rising edge




###message = input("Press enter to quit\n\n") # Run until someone presses enter
##GPIO.cleanup() # Clean up



# loop through stream and append audio chunks to frame array
#for ii in range(0,int((samp_rate/chunk)*record_secs)):
#    data = stream.read(chunk)
#    frames.append(data)

#print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
#stream.stop_stream()
#stream.close()
#audio.terminate()

# save the audio frames as .wav file
#wavefile = wave.open(wav_output_filename,'wb')
#wavefile.setnchannels(chans)
#wavefile.setsampwidth(audio.get_sample_size(form_1))
#wavefile.setframerate(samp_rate)
#wavefile.writeframes(b''.join(frames))
#wavefile.close()

