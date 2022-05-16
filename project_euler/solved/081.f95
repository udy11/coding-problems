	integer*8 mt(80,80)
   open(1,file='81_matrix.txt',status='old')

	do i=1,80
   	read(1,*) (mt(i,j),j=1,80)
   end do

	do k=3,160
		do i=1,80
			j=k-i
         if (j>0 .and. j<81) then
         if(i==1) mt(i,j)=mt(i,j)+mt(i,j-1)
			if(j==1) mt(i,j)=mt(i,j)+mt(i-1,j)
         if(i/=1 .and. j/=1) then
         	if(mt(i,j-1)<mt(i-1,j)) then
            mt(i,j)=mt(i,j)+mt(i,j-1)
            else
            mt(i,j)=mt(i,j)+mt(i-1,j)
            end if
         end if
         end if
      end do
   end do

   print *,mt(80,80)
   end