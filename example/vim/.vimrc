"omnicppcomplete
"set nocp
filetype plugin on
set ofu=syntaxcomplete#Complete
map <C-F12> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q --languages=c++ .<CR>

"taglist
nnoremap <silent> <F8> :TlistToggle<CR>
let Tlist_Inc_Winwidth=0

"generate tags
nnoremap <silent> <F4> :!ptags.py `find . -name "*.py"`<CR>


"set spell
set spelllang=~/.vim/spell/cs.utf-8.spl

"asymptote syntax
augroup filetypedetect
au BufNewFile,BufRead *.asy     setf asy
augroup END
filetype plugin on

" preklad
imap <c-c> <esc>:make<cr>
map  <c-c> :make<cr>

" Octave Syntax
augroup filetypedetect
	au! BufRead,BufNewFile *.m setf octave
augroup END
filetype plugin on

" latex
autocmd BufNewFile,BufRead *.tex source ./.vimrc

" escape from insert mode
imap ;; <Esc>

" Ctrl-j/k inserts line below/above
"nnoremap <silent><C-j> m`:silent +g/\m^\s*$/d<CR>``:noh<CR>
"nnoremap <silent><C-k> m`:silent -g/\m^\s*$/d<CR>``:noh<CR>
nnoremap <silent><C-k> :set paste<CR>m`o<Esc>``:set nopaste<CR>
nnoremap <silent><C-j> :set paste<CR>m`O<Esc>``:set nopaste<CR>

"line breaks
map <S-k> <insert><cr><esc>
