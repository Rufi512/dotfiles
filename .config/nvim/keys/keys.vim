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
:nmap <c-q> :q! <CR>

"Tabs Navigation
:nmap <c-o> :tabp <CR>
:nmap <c-p> :tabn <CR>
:nmap <c-l> :tabnew <CR>

