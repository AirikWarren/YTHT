# YTHT (testing)
Simple Python script that will silently run in the background waiting for the user to copy a YouTube link to their clipboard via ctrl+c and convert the link to either a [invidio.us](invidio.us) or [hooktube](https://hooktube.com) link, circumventing ads and waiving the need to log in to view content that would normally require a sign in due to mature or controversial content. Now defaults to invidio.us as hooktube has been [deprecated](https://archive.fo/RayvP) for all privacy and download related reasons due to issues with YouTube legal and the project's usage of the YouTube API.

If you still wish to you use Hooktube links for whatever reason (it does still appear to edge invidio.us out performance wise) you can do so by running the program with the -ht flag.
## Installation and Use (Unix based Operating Systems) 
`pip install -r requirements.txt`

main.py must be executed as root on most Linux distros due to the keyboard module dependency, it's your responsibility as the user to exercise caution and audit the program as well as it's dependencies (the [pyperclip](https://github.com/asweigart/pyperclip) and [keyboard](https://github.com/boppreh/keyboard) modules) for any potential security flaws that may affect the health and security of your system before use.
