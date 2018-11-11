#!/usr/bin/env python
import pyperclip
import keyboard
import sys


def main():
        print("STARTING. . .")
        keyboard.add_hotkey(
                'ctrl+c',
                paste_replacement_url_to_clipboard,
                args=[parse_cli_args()]
        )
        keyboard.wait('ctrl+q')
        print("QUITTING. . .")


def parse_cli_args():
        try:
            if sys.argv[1] == '-ht' or sys.argv[1] == '--hooktube':
                print('Hooktube mode initialized')
                return 'hooktube.com'
            else:
                print('Only accepts the -ht or --hooktube flag as an argument')
                print('Defaulting to invidio.us mode')
                return 'invidio.us'
        except IndexError:
            return 'invidio.us'


def paste_replacement_url_to_clipboard(replacement_url):
        replacement_url = convert_yt_url(pyperclip.paste(), replacement_url)
        pyperclip.copy(replacement_url)


def convert_yt_url(url, replacement_url):
        if 'youtube' in url:
                return url.replace('youtube.com', replacement_url)
        elif 'youtu.be' in url:
                return url.replace('youtu.be', replacement_url)
        else:
                return url


if __name__ == '__main__':
        main()
