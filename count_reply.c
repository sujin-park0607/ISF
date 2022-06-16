#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <io.h> 


typedef struct _finddata_t FILE_SEARCH;


void GetfileList(char * path) {
	FILE * read1;
	FILE * read2;
	char dum[4096];
	char sPath[1024] = "";
	char seps[] = ",";
	char *token;
	int row, col, N_row, N_col;
	double *pos, **data;
	double ddd;
	int i;
	
	
  long h_file;
  char search_Path[100];
  FILE_SEARCH file_search;
  sprintf(search_Path, "%s/*.*", path);
  if ((h_file = _findfirst(search_Path, & file_search)) == -1L)
  {
    printf("No files in current directory!\n");
  }
  else {
    do {
    	for(i=0 ; i<1024 ; i++){
    		sPath[i] = '\0';
		}
		printf("%s\t¡æ\t", file_search.name);
		strcat(sPath, "C:/Users/acin/Desktop/news/");
		strcat(sPath, file_search.name);
		
		read1 = fopen(sPath,"rt");	
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
      
    } while (_findnext(h_file, & file_search) == 0);
    _findclose(h_file);
  }
}

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
	
	
	//
	GetfileList("C:/Users/acin/Desktop/news");
	return 0;
	//
	
	
	
	read1 = fopen("20210622.csv","rt");
	
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
