from gpiozero import Button
from enum import Enum


class RecMode(Enum):
  INACTIVE = 0
  MODE1 = 1
  MODE2 = 2



class ButtonController:
    """  """

    _button_mode1_pin = 23
    _button_mode2_pin = 24

    # instantiate buttons
    _button_mode1 = Button(pin = _button_mode1_pin, pull_up = None,  active_state = True)
    _button_mode2 = Button(pin = _button_mode2_pin, pull_up = None,  active_state = True)
    _start_handler = None
    _stop_handler = None
    _recording_mode = RecMode.INACTIVE

    def __init__(self, startHandler, stopHandler):
      #  assign button dandler
      self._button_mode1.when_pressed = self.button_press_handler
      self._button_mode1.when_released = self.button_release_handler
      self._button_mode2.when_pressed = self.button_press_handler
      self._button_mode2.when_released = self.button_release_handler
      # store external handler
      self._start_handler = startHandler
      self._stop_handler = stopHandler
      

    def __del__(self): 
      # release pins when destructing the object
      self._button_mode1.close()
      self._button_mode2.close() 


    def button_press_handler(self,pressed_button):
      # handle button presses
      if self._recording_mode == RecMode.INACTIVE:
        # only if recording mode is inactive
        switch (pressed_button.pin.number) {
          case self._button_mode1_pin:
            # mode1 button pressed
            self._recording_mode = RecMode.MODE1
            startHandler(self._recording_mode)
            break
          case self._button_mode2_pin:
            # mode2 button pressed
            self._recording_mode = RecMode.MODE2
            startHandler(self._recording_mode)
            break
        }



    def button_release_handler(self,pressed_button): 
      # handle button releases
      if (pressed_button.pin.number == self._button_mode1_pin) and (self._recording_mode == RecMode.MODE1):
        # only react on releases of mode1 button if we are in mode1
        self._recording_mode = RecMode.INACTIVE
        stopHandler()
      if (pressed_button.pin.number == self._button_mode2_pin) and (self._recording_mode == RecMode.MODE2):
        # only react on releases of mode2 button if we aree in mode2
        self._recording_mode = RecMode.INACTIVE
        stopHandler()

   



def startHandler(mode):
  print(f"startHandler {mode.name}")

def stopHandler():
  print("stopHandler")  



def main():
  button_controller = ButtonController(startHandler, stopHandler)

  try:
    while True:
      pass

  except KeyboardInterrupt:
    pass

  finally:
    del button_press_handler







if __name__ == "__main__":
    main()

