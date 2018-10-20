#!/usr/bin/env python
import pyperclip
import keyboard


def main():
        keyboard.add_hotkey('ctrl+c', paste_hooktube_url_to_clipboard)
        keyboard.wait('ctrl+q')
        print("quitting. . .")


def paste_hooktube_url_to_clipboard():
        hooktube_url = convert_yt_url(pyperclip.paste())
        pyperclip.copy(hooktube_url)


def convert_yt_url(url):
        if 'youtube' in url:
                return url.replace('youtube', 'hooktube')
        elif 'youtu.be' in url:
                return url.replace('youtu.be', 'hooktube.com')
        else:
                return url


if __name__ == '__main__':
        main()
