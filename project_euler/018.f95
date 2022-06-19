! the minute cleverness needed is to begin from
! last row and keep on updating the upper rows

	integer n(15,15),rw
   rw=15
	open(1,file='018_data.dat',status='old')
   do i=1,rw
   	read(1,*) (n(i,j),j=1,i)
   end do

	do i=rw,2,-1
   	do j=1,i-1
      	if(n(i,j)>n(i,j+1)) then
         n(i-1,j)=n(i-1,j)+n(i,j)
         else
         n(i-1,j)=n(i-1,j)+n(i,j+1)
         end if
      end do
   end do

	print *,n(1,1)
   end