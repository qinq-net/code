/*
 * =====================================================================================
 *
 *       Filename:  lan_2.c
 *
 *    Description:  swap(int *a, int *b); swap two integers
 *
 *        Version:  1.0
 *        Created:  10/22/2015 02:55:54 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  School of Physics and Nuclear Energy
 *                  Engineering
 *   Organization:  Beihang University
 *
 * =====================================================================================
 */

void swap(int *a, int *b)
{
	*a=*a+*b;
	*b=*a-*b;
	*a=*a-*b;
}

