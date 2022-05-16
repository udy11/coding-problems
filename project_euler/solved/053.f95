	integer*8 n,r,fact
   c=0
   do n=1,100
   	do r=1,n
      	if(fact(n)/fact(r)/fact(n-r)>1000000) then
         c=c+1
         end if
		end do
	end do
   print *,c
   end


	integer*8 function fact(n)
   integer*8 n,p,i
   fact=n
   if(n>1) then
   do i=2,n-1
   	fact=fact*i
   end do
   else
   fact=1
   end if   
   end