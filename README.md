[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# ncm2-github-emoji
GitHub emoji source for [NCM2](https://github.com/ncm2/ncm2)

## Installation

### Basic installation

Install it like you would install any other plugin. Then, at the plugin's installation directory (i.e. which contains `install.py`) run the following commands -
```
python -m pip install requests
python install.py
```

This pulls the latest emojis from GitHub's API and **creates the actual plugin** file.

### Advanced installation (using plugin managers)

Some notes -
* If `pip` is executable and in your `PATH`, you can directly run `install.py` without caring about `requests`
* If you use plugin managers, it can probably run a command after the plugin is installed/updated

So, you can simply do something like this (example is of [vim-plug](https://github.com/junegunn/vim-plug))
```
Plug 'subnut/ncm2-github-emoji', { 'do': './install.py' }
```

And the plugin manager shall take care of all the above stuff itself. Every time the plugin updates. Yay!
