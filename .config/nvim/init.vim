"--AutoComplete--

filetype plugin on
autocmd FileType css set omnifunc=syntaxcomplete#Complete

source $HOME/.config/nvim/vim-plug/plugins.vim

source $HOME/.config/nvim/themes/oceaNext.vim

source $HOME/.config/nvim/plug-config/coc.vim

source $HOME/.config/nvim/keys/keys.vim

source $HOME/.config/nvim/general/settings.vim

source $HOME/.config/nvim/plug-config/vim-devicons.vim

source $HOME/.config/nvim/plug-config/emmet.vim

source $HOME/.config/nvim/plug-config/prettier.vim
hi NonText ctermbg=none
hi Normal guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE 
highlight Normal     ctermbg=NONE guibg=NONE
highlight LineNr     ctermbg=NONE guibg=NONE
highlight SignColumn ctermbg=NONE guibg=NONE
