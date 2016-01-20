/*
 * =====================================================================================
 *
 *       Filename:  hex.c
 *
 *    Description:  Scan a string for hex
 *
 *        Version:  1.0
 *        Created:  10/27/2015 10:08:40 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Qin Yuhao
 *   Organization:  Beihang University
 *
 * =====================================================================================
 */
#include "hex.h"
long long int convert(char *str, int buf)
{
	if(*str!='0')
	{
		//return dec(str, buf);
	}
	if(*(++str)!='x')
	{
		//return ord(str, buf-1);
	}
	return hex(++str, buf-2);

}
long long int hex(char * str, int buf)
{
	long long int res=0;
	for(;buf;buf--,str++)
	{
		if(*str>='0'&&*str<='9') res = (res << 4) + (*str - '0');
		else if(*str>='a'&&*str<='f') res = (res << 4) + (*str - 'a' + 11);
		else if(*str>='A'&&*str<='F') res = (res << 4) + (*str - 'A' + 11);
		else break;
	}
	return res;
}
