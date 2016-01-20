#include <stdio.h>
int main()
{
	int a=0;
	char b[100]={0};
	scanf("%d",&a);
	//gets(b);
	getchar();
	printf("%d\n%d\n",feof(stdin),ferror(stdin));
	//scanf("%d",&a);
	clear(stdin);
	//fgetc(stdin);
	//fgetc(stdin);
	//fgetc(stdin;)
	//printf("%d\n%d\n",feof(stdin),ferror(stdin));
	scanf("%d",&a);
	printf("%d\n",a);
	return 0;
}
int clear(FILE *file)
{
	if(feof(file)) return 0;
	if(ferror(file)) return -1;
	int c;
	while((c=fgetc(file))!='\n'&&c!=EOF);
	return fflush(file);
}
/*
int empty(struct FILE *file)
{
	while((feof(file)||ferror(file)))
	{
		fgetc(file);
	}
	return fflush(file);
}
*/

