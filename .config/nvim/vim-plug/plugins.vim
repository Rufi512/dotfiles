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
    "Explore files
    Plug 'Shougo/unite.vim'
    Plug 'Shougo/vimfiler.vim'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'
    " ColorSchemes
    Plug 'joshdick/onedark.vim'
    Plug 'mhartington/oceanic-next'
    Plug 'pgavlin/pulumi.vim'
    Plug 'bluz71/vim-nightfly-guicolors'
    Plug 'flrnd/candid.vim'
    " Intellisense
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    "Vim-visual-multi
    Plug 'mg979/vim-visual-multi', {'branch': 'master'}
    "Vim-Airline
    Plug 'vim-airline/vim-airline'
    "MatchTagAlways
    Plug 'Valloric/MatchTagAlways' 
    "Vim syntax JS
    Plug 'pangloss/vim-javascript'
    "Emmet
    Plug 'mattn/emmet-vim'
    "Prettier
    Plug 'prettier/vim-prettier', { 'do': 'npm install' }
    "Indent
    Plug 'Yggdroot/indentLine' 
    "Devicons
    Plug 'ryanoasis/vim-devicons'
    call plug#end()
