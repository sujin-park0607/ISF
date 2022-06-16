#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE * read1;
	FILE * read2;
	char dum[4096];
	char seps[] = ",";
	char *token;
	int row, col, N_row, N_col;
	double *pos, **data;
	double ddd;
	//
	//	

	read2 = fopen("20210622.csv","rt");
	row = 0;	
	while (fgets(dum,4096, read1) != NULL)
	{	
		col = 0;		
		token = strtok(dum, seps);
		while (token != NULL)
		{
			col++;
			token = strtok(NULL, seps);
		}
		row++;
	}	
        N_row = row;
	N_col = col;
	printf("ROW: %d \t COL: %d \n", N_row, N_col);
	fclose(read1);
}
