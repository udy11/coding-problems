	integer*8 mt(80,80),mtn(80,80),fmn,sm,min
   open(1,file='82_matrix.txt',status='old')

	do i=1,80
   	read(1,*) (mt(i,j),j=1,80)
   end do
   mtn=mt

   do j=2,80
	do i=1,80
		min=mtn(i,j-1)
		do k=1,80
      	sm=mtn(k,j-1)
			do m=0,iabs(k-i)-1
				sm=sm+mtn(k+(i-k)*m/iabs(i-k),j)
         end do
			if(sm<min) min=sm
      end do
      mt(i,j)=mt(i,j)+min
	end do
  	do l=1,80
     	mtn(l,j)=mt(l,j)
	end do
   end do

	fmn=mt(1,80)
	do i=2,80
   	if(mt(i,80)<fmn) fmn=mt(i,80)
   end do
   
   print *,fmn
   end