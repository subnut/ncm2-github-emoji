[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# ncm2-github-emoji
GitHub emoji source for [NCM2](https://github.com/ncm2/ncm2)

## Installation

### Basic installation

Install it like you would install any other plugin. Then, at the plugin's installation directory (i.e. which contains `install.py`) run the following command -
```
python install.py
```
This pulls the latest emojis from GitHub's API and **creates the actual plugin** file.


### Installation using plugin managers
Some plugin managers support running a command after a plugin has been installed. Check with the plugin developer if yours supports it. If yes, you can simply do something like this (example is of [vim-plug](https://github.com/junegunn/vim-plug))
```
Plug 'subnut/ncm2-github-emoji', { 'do': 'python install.py' }
```

<br/>

## Known Issues
* Preview does not work for GitHub-special emojis
