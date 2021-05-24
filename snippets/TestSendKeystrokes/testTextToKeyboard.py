import argparse
import sendString




def main():
    parser = argparse.ArgumentParser(description='Running SendText to HID device.')

    parser.add_argument('--text', required=True,
                        help='text to send')
    args = parser.parse_args()

    sendString.send(args.text)



if __name__ == '__main__':
    main()
