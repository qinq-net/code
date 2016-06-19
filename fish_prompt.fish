# vim: set noet:
#
# Set the default prompt command.


function fish_prompt --description "Write out the prompt"
	# Just calculate this once, to save a few cycles when displaying the prompt
	if not set -q __fish_prompt_hostname
		set -g __fish_prompt_hostname (hostname|cut -d . -f 1)
	end

	set -l color_cwd
	set -l suffix
	switch $USER
	case root toor
		if set -q fish_color_cwd_root
			set color_cwd $fish_color_cwd_root
		else
			set color_cwd $fish_color_cwd
		end
		set suffix '#'
	case '*'
		set color_cwd $fish_color_cwd
		set suffix '$'
	end
	
	export __fish_git_prompt_showcolorhints=1
	export __fish_git_prompt_show_informative_status=1
	export fish_prompt_pwd_dir_length=0

	echo -s (set_color $fish_color_operator) "╔═[" \
		(set_color $fish_color_user) "$USER" \
		(set_color $fish_color_autosuggestion) "@" \
		(set_color $fish_color_host) "$__fish_prompt_hostname" \
		(set_color $fish_color_operator) "] " \
		(set_color normal) "-" \
		(set_color $fish_color_operator) " [" \
		(set_color $fish_color_quote) (date +"%a %b %d, %k:%M") \
		(set_color $fish_color_operator) "]"
	echo -s (set_color $fish_color_operator) "╚╦─[" \
		(set_color $color_cwd) (prompt_pwd) \
		(set_color $fish_color_operator) "] <" \
		(set_color normal) (__fish_svn_prompt) \
		(set_color normal) (__fish_git_prompt "(%s)") \
		(set_color $fish_color_operator) ">"
	echo -n -s (set_color $fish_color_operator) " ╚═[" (set_color normal) "$suffix" (set_color $fish_color_operator) "] " (set_color normal) 
end
