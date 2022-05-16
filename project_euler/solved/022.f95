	integer*8 s
	CHARACTER*11 c(5163)
   open(1,file='022_names_az_5163.txt')
   do i=1,5163
		read(1,*) c(i)
   end do

	s=0
	do j=1,5163
	do i=1,11
   if(c(j)(i:i)/=' ') s=s+(IACHAR(c(j)(i:i))-64)*j
   end do
   end do

   print *,s
   end
