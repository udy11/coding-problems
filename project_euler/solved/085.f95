	integer*8 i,j,p
   open(1,file='085_out.txt')
	do i=1,200
   do j=1,200
   	p=i*j
   	write(1,*) i,j,p*(p+i+1+j)/4
   end do
   end do
   end