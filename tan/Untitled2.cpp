#include <stdio.h>
#include <conio.h>
struct sinhvien
{
	char masv[15];
	char tensv[50];
	float diem;
};
int main()
{
sinhvien sv[30];
int i, n;
float a;
printf("nhap so sinh vien n= ");
scanf("%d",&n);
printf("\nnhap danh sach sinh vien");
for(i=0;i<n;i++)
{
	printf("\nthong tin thu %d la: \n",i+1);
	printf("ma sv: "); 			fflush(stdin);/* xoa bo nho dem tranh choi du lieu */	gets(sv[i].masv);
	printf("\nho ten sv: ");	fflush(stdin);	gets(sv[i].tensv);
	printf("\nDiem TB = ");			scanf("%f",&a); sv[i].diem=a;
}
printf("danh sach nhan vien vua nhap \n");
printf("ma \t ho va ten \t Diem tb\n");
for(i=0;i<n;i++)
{
	printf("%s \t %s\t  %f\n",sv[i].masv,sv[i].tensv,sv[i].diem);
}
printf("danh sach sinh vien co diem tb >5: \n");
printf("ma \t ho va ten \t Diem tb \n");
for(i=0;i<n;i++)
{
if(sv[i].tensv=="Nguyen Van Ai")
	printf("%s \t %s\t %f\n",sv[i].masv,sv[i].tensv,sv[i].diem);
}


return 0;
}
