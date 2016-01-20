#include <stdio.h>
#include <string.h>

int main(int argc, char ** argv)
{
	char a[2048] = { 0 };
	gets(a);
	printf("%s\n", a);
	return 0;
}
