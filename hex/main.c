/*
 * =====================================================================================
 *
 *       Filename:  main.c
 *
 *    Description:  usage
 *
 *        Version:  1.0
 *        Created:  10/27/2015 10:53:54 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdio.h>
#include "hex.h"
int main(int argc, char **argv)
{
	char a[20]={0};
	fgets(a,20,stdin);
	printf("%lld",convert(a,20));
	return 0;
}
