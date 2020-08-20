# ncm2-github-emoji [![Github repo link](https://img.shields.io/badge/view%20on%20github-black?style=for-the-badge&logo=github)](https://github.com/subnut/ncm2-github-emoji "Github repo link")
<p align="center">
<img alt="Windows" src="https://img.shields.io/badge/Windows-brightgreen?style=for-the-badge&logo=windows&logoColor=white&color=0078D6">
<img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black&color=EBB513">
<img alt="macOS" src="https://img.shields.io/badge/macOS-999999?style=for-the-badge&logo=apple&logoColor=white&color=999999">
<a href="https://neovim.io"><img alt="neovim" src="https://img.shields.io/badge/neovim-57A143?style=for-the-badge&logo=neovim&logoColor=white"></a>
<br/>
<a href="https://github.com/subnut/ncm2-github-emoji"><img alt="GitHub stars" src="https://img.shields.io/github/stars/subnut/ncm2-github-emoji?style=for-the-badge&logo=github"></a>
<a href="https://github.com/subnut/ncm2-github-emoji/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/subnut/ncm2-github-emoji?style=for-the-badge&logo=github"></a>
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/subnut/ncm2-github-emoji/Check%20if%20install.py%20can%20run%20without%20requests%20module%20pre-installed/master?style=for-the-badge&logo=github">
<br/>
<a href="https://github.com/subnut"><img alt="Author" src="https://img.shields.io/badge/Author-subnut-brightgreen?style=for-the-badge&logo=github"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-lightgrey?style=for-the-badge&color=000"></a>
<a href="https://github.com/subnut/ncm2-github-emoji/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/subnut/ncm2-github-emoji?style=for-the-badge"></a>
</p>
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
