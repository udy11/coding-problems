	integer f(1000,3)

	do i=1,1000
		do k=1,3
      	f(i,k)=0
      end do
   end do
   f(1,1)=1; f(1,2)=1; s=0; c=2

   while(f(1000,3)==0) do
		s=0
		do i=1,1000
      	f(i,3)=s+f(i,1)+f(i,2)
	      s=f(i,3)/10
	      f(i,3)=mod(f(i,3),10)
         f(i,1)=f(i,2)
         f(i,2)=f(i,3)
      end do
      c=c+1
   end while
   print *,c
   end