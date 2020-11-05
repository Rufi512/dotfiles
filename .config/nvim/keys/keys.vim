"Save File : ctrl + s
:nmap <c-s> :w<CR>
:imap <c-s> <Esc>:w<CR>a

"Explore File
:nmap <c-e> :Explore<CR>

"Escape
:nmap <C-c> <ESC>

"TAB completion
:nmap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"

"Quit nvim
:nmap <c-q> :wq! <CR>

