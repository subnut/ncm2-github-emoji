# ncm2-github-emoji
<span style="display:block;text-align:center">

[![GitHub stars](https://img.shields.io/github/stars/subnut/ncm2-github-emoji?style=for-the-badge&logo=github)](https://github.com/subnut/ncm2-github-emoji) [![GitHub issues](https://img.shields.io/github/issues/subnut/ncm2-github-emoji?style=for-the-badge&logo=github)](https://github.com/subnut/ncm2-github-emoji/issues) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/subnut/ncm2-github-emoji/Check%20if%20install.py%20can%20run%20without%20requests%20module%20pre-installed/master?style=for-the-badge&logo=github)
<br/>
![Windows](https://img.shields.io/badge/Windows-supported-brightgreen?style=for-the-badge&logo=windows&logoColor=white&color=0078D6) ![Linux](https://img.shields.io/badge/Linux-supported-FCC624?style=for-the-badge&logo=linux&logoColor=white&color=FCC624) ![macOS](https://img.shields.io/badge/macOS-supported-999999?style=for-the-badge&logo=apple&logoColor=white&color=999999)
<br/>
![Neovim](https://img.shields.io/badge/Neovim-Tested-brightgreen?style=for-the-badge&logo=neovim&logoColor=brightgreen) [![Code style: black](https://img.shields.io/badge/code%20style-black-lightgrey?style=for-the-badge&color=000)](https://github.com/psf/black) [![GitHub license](https://img.shields.io/github/license/subnut/ncm2-github-emoji?style=for-the-badge)](https://github.com/subnut/ncm2-github-emoji/blob/master/LICENSE)

</span>
<br/>

GitHub emoji source for [NCM2](https://github.com/ncm2/ncm2)

<p align="center">
<img src="screenshot.png" caption="Screenshot" alt="screenshot">
</p>

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
