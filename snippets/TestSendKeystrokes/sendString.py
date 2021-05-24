import os
import hid

hid_path = os.environ.get('HID_PATH', '/dev/hidg0')


# control keys - these are represented by bits in a integer value
control_key_none = 0  # no bits set
control_key_ctrl = 1  # bit 1 on true
control_key_shift = 2  # bit 2 on true
control_key_alt = 4  # bit 3 on true
control_key_meta = 8  # bit 4 on true

# HID keycodes source: https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
_LETTER_TO_HID_KEYCODES = {
    ' ': 0x2c,  # Spacebar
    'a': 0x04,  # a
    'b': 0x05,  # b
    'c': 0x06,  # c
    'd': 0x07,  # d
    'e': 0x08,  # e
    'f': 0x09,  # f
    'g': 0x0a,  # g
    'h': 0x0b,  # h
    'i': 0x0c,  # i
    'j': 0x0d,  # j
    'k': 0x0e,  # k
    'l': 0x0f,  # l
    'm': 0x10,  # m
    'n': 0x11,  # n
    'o': 0x12,  # o
    'p': 0x13,  # p
    'q': 0x14,  # q
    'r': 0x15,  # r
    's': 0x16,  # s
    't': 0x17,  # t
    'u': 0x18,  # u
    'v': 0x19,  # v
    'w': 0x1a,  # w
    'x': 0x1b,  # x
    'y': 0x1c,  # y
    'z': 0x1d,  # z
}


def send(text):
    # Iterate over the string
    for element in text:
      if element.isupper():
        control_keys = control_key_shift
      else:
        control_keys = control_key_none
      hid_keycode = _LETTER_TO_HID_KEYCODES[element.lower()]
      hid.send(hid_path, control_keys, hid_keycode)


