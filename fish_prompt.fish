#!/usr/bin/env fish
# vim: set et ts=4 ft=sh:
#
# Set the default prompt command.

function stringwidth
    if perl -MText::CharWidth -e 1 -X 2>/dev/null
        perl -MText::CharWidth=mbswidth -le 'print mbswidth shift' "$argv"
    else if perl -MText::CharWidth::PurePerl -e 1 -X 2>/dev/null
        perl -MText::CharWidth::PurePerl=mbswidth -le 'print mbswidth shift' "$argv"
    else
        if which gexpr 2>/dev/null; alias __EXPR=gexpr; else; alias __EXPR=expr; end
        __EXPR length "$argv"
    end
end

function sw
	stringwidth (echo $argv|sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g")
end

function iamroot
	if [ ( uname|grep -qE "NT" ) ]
		id -G |grep -qE '\<544\>'
	else
		[ (id -u) -eq 0 ]
	end if
end

function fish_prompt --description "Write out the prompt"
	export __status=$status # must be first line of function
    echo -ns (set_color $fish_color_comment) "." >&2; # show some dots

	# Just calculate this once, to save a few cycles when displaying the prompt
	if not set -q __fish_prompt_hostname
		set -g __fish_prompt_hostname (hostname|cut -d . -f 1)
	end
	set -x USER (whoami)
	set -l color_cwd
	set -l suffix
    set -l color_cwd_root
	if set -q fish_color_cwd_root
		set color_cwd_root $fish_color_cwd_root
	else
		set color_cwd_root $fish_color_error
	end

#	switch $USER
#	case root toor
	if iamroot
        set color_cwd $color_cwd_root
		set suffix '#'
#	case '*'
	else
		set color_cwd $fish_color_cwd
		set suffix '$'
	end
    echo -ns "." >&2

	export __fish_git_prompt_showcolorhints=1
	export __fish_git_prompt_show_informative_status=1
	export fish_prompt_pwd_dir_length=0

	if [ "$COLUMNS" -gt "60" ];
		echo -s (set_color $fish_color_operator) "╔═[" \
			(set_color $fish_color_user) "$USER" \
			(set_color $fish_color_autosuggestion) "@" \
			(set_color $fish_color_host) "$__fish_prompt_hostname" \
			(set_color $fish_color_operator) "] " \
			(set_color normal) "-" \
			(set_color $fish_color_operator) " [" \
			(set_color $fish_color_quote) (date +"%a %b %d, %k:%M") \
			(set_color $fish_color_operator) "] "
	else
		echo -s (set_color $fish_color_operator) "╔═[" \
			(set_color $fish_color_user) "$USER" \
			(set_color $fish_color_autosuggestion) "@" \
			(set_color $fish_color_host) "$__fish_prompt_hostname" \
			(set_color $fish_color_operator) "] "
	end
    echo -ns "." >&2
	
    set prompt_versioncon 	(echo -sn 	(timeout 1.5s fish -c "echo -s (__fish_vcs_prompt)")|sed 's/ //g')
	export long_prompt_line2=( export fish_prompt_pwd_dir_length=0;
				echo -s (set_color $fish_color_operator) "╚╦─[" \
					(set_color $color_cwd) (prompt_pwd) \
					(set_color $fish_color_operator) "] <" \
					(set_color normal) "$prompt_versioncon" \
					(set_color $fish_color_operator) "> " )
	export short_prompt_line2=( export fish_prompt_pwd_dir_length=1;
				echo -s (set_color $fish_color_operator) "╚╦─[" \
					(set_color $color_cwd) (prompt_pwd) \
					(set_color $fish_color_operator) "] <" \
					(set_color normal) "$prompt_versioncon" \
					(set_color $fish_color_operator) "> " )
    echo -ns "." >&2

	#if [ (expr length (echo -n "$long_prompt_line2"|sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g")) -gt "$COLUMNS" ];
	#	if [ (expr length (echo -n "$short_prompt_line2"|sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g")) -gt "$COLUMNS" ];
	if [ (sw "$long_prompt_line2") -gt "$COLUMNS" ];
		if [ (sw "$short_prompt_line2") -gt "$COLUMNS" ];
			echo -s (set_color $fish_color_operator) "╚╦─[...] <" \
                    (set_color normal) "$prompt_versioncon" \
                    (set_color $fish_color_operator) "> "
		else
			echo "$short_prompt_line2"
		end
	else
		echo "$long_prompt_line2"
	end
    echo -ns "." >&2
	
	echo -n -s \
		(set_color $fish_color_operator) " ╚═[" \
		(set_color normal) "$suffix" \
		(set_color $fish_color_operator) "] <" \
		(if [ $__status -eq 0 ]; set_color normal; else; set_color $fish_color_error; end) $__status \
		(set_color $fish_color_operator) "> " \
		(set_color normal) 
    #echo -en "\r\033[K" >&2
    echo -en "\b\b\b\b\b\033[K" >&2
end
