/*
 * =====================================================================================
 *
 *       Filename:  test2.c
 *
 *    Description:  hehe.
 *
 *        Version:  1.0
 *        Created:  10/23/2015 02:18:35 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdio.h>
int main(int argc, char **argv)
{
	typedef union{
		long long int a;
		double b;
	} k;
	//printf("%d, %d\n",sizeof(double),sizeof(long long int));
	k b;
	b.b=2.340;
	printf("%llx\n",b.a);
	return 0;
}
