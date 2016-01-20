#include<stdio.h>
int main()
{
    char op;
    int d1,d2;
    scanf("%d %d %c",&d1,&d2,&op);
    switch(op)
	{
	case '+':
		{
		int con;
		con=d1+d2;
		printf("%d",con);
		break;
		}
	case '-':
		{
		int con;
		con=d1-d2;
		printf("%d",con);
		break;
		}
	case '*':
		{
		int con;
		con=d1*d2;
		printf("%d",con);
        break;
		}
	case '/':
		{
		if(d1/d2)
		{
			double con;
			con=(double)d1/d2;
			printf("%.2f",con);
		}
	    else
		{
			int con;
			con=d1/d2;
			printf("%d",con);
		}
		break;
		}
	default:printf("end");
		putchar(op);
		putchar(':');
	}
}
