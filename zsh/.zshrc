source ~/.zsh/antigen.zsh

# Preload
export PATH=/home/shanril/.local/bin:$PATH
export PATH=/home/shanril/bin:$PATH
export TERM="xterm-256color"

#Aliases

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).

# Syntax highlighting bundle.
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions

#Load theme
antigen theme agnoster

# Tell Antigen that you're done.
antigen apply