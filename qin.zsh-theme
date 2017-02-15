#!/usr/bin/env zsh
# vim: set et ts=2 sw=2 ft=sh:
# user, host, full path, and time/date
# on three lines for easier vgrepping
precmd() {
    __exit_status=$?
    if $ran_something; then
        exit_status=$__exit_status
    fi
    ran_something=false
}
preexec() {
    ran_something=true
}
show_non_zero_exit_status() {
    case $exit_status in
    0|20|148)
        echo "%{\e[1;35m%}$exit_status";;
    *)
        echo "%{\e[5;31m%}$exit_status";;
    esac
}
iamroot(){
  if [ ` uname|grep -qE "NT" ` ];then
    id -G |grep -qE '\<544\>'
  else [ `id -u` -eq 0 ]
  fi
}
prompt_sign(){
 if iamroot
   then echo "%{\e[1;5;31m%}#"
 else echo "%{\e[1;35m%}$"
 fi
}
GET_PROMPT_INFO=y
get_prompt_info(){
 if [ 'y' = ''$GET_PROMPT_INFO ]; then
  GIT_PROMPT_INFO=`git_prompt_info`
  SVN_PROMPT_INFO=`svn_prompt_info`
  if [ '' = ''$GIT_PROMPT_INFO ]; then
   PROMPT_INFO='%{\e[0;33m%}%B'$SVN_PROMPT_INFO
  else; if [ '' = ''$SVN_PROMPT_INFO ]; then
   PROMPT_INFO='%{\e[0;36m%}%B'$GIT_PROMPT_INFO
  else PROMPT_INFO="%{\e[0;36m%}%B"$GIT_PROMPT_INFO"%{\e[0;0m%}%B|%{\e[0;33m%}%B"$SVN_PROMPT_INFO
  fi;fi
 else
  PROMPT_INFO=
 fi
 echo $PROMPT_INFO
}
prompt(){
setopt promptsubst
export PROMPT=\
$'%{\e[0;34m%}%B╔═[%b%{\e[0m%}%{\e[1;32m%}$(id -un)%{\e[1;30m%}@%{\e[0m%}%{\e[0;36m%}$(hostname)%{\e[0;34m%}%B]%b%{\e[0m%} - %{\e[0;34m%}%B[%b%{\e[0;33m%}'%D{"%a %b %d, %K:%M"}%b$'%{\e[0;34m%}%B]%b%{\e[0m%}
%{\e[0;34m%}%B╚╦─%b%{\e[0;34m%}%B[%b%{\e[1;37m%}%~%{\e[0;34m%}%B] %{\e[0;35m%}%B<%{\e[1;33m%}$(get_prompt_info)%{\e[0;35m%}%B>%b%{\e[0m%}
%{\e[0;34m%}%B ╚═%B[%{\e[1;35m%}$(prompt_sign)%{\e[0;34m%}%B] %B<$(show_non_zero_exit_status)%{\e[0;34m%}%B> %{\e[0m%}%b'
export PS2=$' \e[0;34m%}%B>%{\e[0m%}%b '
}
prompt

