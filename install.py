#!/bin/python3

requests_installed = False
try:
    import requests
except ModuleNotFoundError:
    print("'requests' module is needed to run install.py")
    print("Trying to install it ...")
    from subprocess import PIPE, Popen

    process = Popen(
        ["python", "-m", "pip", "install", "requests"],
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )
    stdout, stderr = process.communicate()
    exitcode = process.returncode
    if exitcode != 0:
        print(
            """Could not install
Please install the 'requests' module and re-run this script"""
        )
        exit(1)
    requests_installed = True
    print("Installed successfully!")

from requests import get

# the API is inconsistent.
# So remove all \n, and also remove the { and } from the beginning and the end
api_response = get("https://api.github.com/emojis").text.replace("\n", "")[1:-1]
emoji_list = api_response.split(",")

final = ""
for entry in emoji_list:
    shortcode_raw, https, url = entry.split(":")
    shortcode_raw = shortcode_raw.strip()
    shortcode_raw = shortcode_raw.strip('"')
    shortcode = ":" + shortcode_raw + ":"
    codepoint_list = url[url.rfind("/") + 1 : url.find(".png")].split("-")
    codepoint = r""
    for point in codepoint_list:
        codepoint += r"\U" + point
    if codepoint.replace("\\", "").replace(" ", "")[:-1].isalpha():
        # GitHub special - No unicode codepoint
        codepoint = "' '"
    else:
        codepoint = '"' + codepoint + ' "'
    final += "\n" + r"\ {'word': '" + shortcode + r"', 'menu': " + codepoint + "},"

to_write = (
    r"""if get(s:, 'loaded', 0)
    finish
endif
let s:loaded = 1

let g:ncm2_github_emoji#proc = yarp#py3('ncm2_github_emoji')
let g:ncm2_github_emoji#proc.on_load = 'ncm2_github_emoji#on_load'

func! ncm2_github_emoji#init() abort
    call ncm2#register_source(g:ncm2_github_emoji#emoji_source)
endfunc

func! ncm2_github_emoji#on_warmup(ctx) abort
    call g:ncm2_github_emoji#proc.jobstart()
endfunc

" emoji

" # character doesn't work well with abbreviation match
let g:ncm2_github_emoji#emoji_source = extend(
                        \ get(g:, 'ncm2_github_emoji#emoji_source', {}), {
            \ 'name': 'github-emoji',
            \ 'scope': ['gitcommit', 'markdown', 'magit'],
            \ 'priority': 0,
            \ 'mark': 'ghe',
            \ 'on_complete': 'ncm2_github_emoji#on_complete_emoji',
            \ 'word_pattern': ':[\w+-]*:?',
            \ 'complete_length': 1,
            \ }, 'keep')

func! ncm2_github_emoji#on_complete_emoji(ctx) abort
    let matches = ["""
    + final
    + r"""
\ ]
        call ncm2#complete(a:ctx, a:ctx.startccol, matches)
endfunc"""
)

try:
    open("autoload/ncm2_github_emoji.vim").close()
except FileNotFoundError:
    import os

    os.mkdir("autoload")
finally:
    with open("autoload/ncm2_github_emoji.vim", "w") as write_file:
        write_file.write(to_write)

if requests_installed:
    print("Requests was installed. Uninstalling it ...")
    process = Popen(
        ["python", "-m", "pip", "uninstall", "requests", "-y"],
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )
    stdout, stderr = process.communicate()
    exitcode = process.returncode
    if exitcode != 0:
        exit(10)
    else:
        print("Uninstalled successfully")
