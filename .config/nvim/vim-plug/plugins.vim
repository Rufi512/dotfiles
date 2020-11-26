" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " ColorSchemes
    Plug 'joshdick/onedark.vim'
    Plug 'mhartington/oceanic-next'
    " Intellisense
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    "Vim-visual-multi
    Plug 'mg979/vim-visual-multi', {'branch': 'master'}
    "Vim-Airline
    Plug 'vim-airline/vim-airline'
    "Vim syntax JS
    Plug 'pangloss/vim-javascript'
    "html5
    Plug 'othree/html5.vim'
    call plug#end()
