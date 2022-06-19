	integer m(10000),s,tm,d
   s=0
	do i=1,10000
   	m(i)=i
   end do
   do i=2,10000
   	if(m(i)/=0) then
      tm=d(m(i))
      if(d(tm)==m(i) .and. tm/=m(i)) then
      	s=s+m(i)+tm
         print *,m(i),tm
         m(tm)=0
      end if
      end if
   end do
   print *,s
   end

	integer function d(n)
   d=1; i=2
   while(i<=sqrt(n*1.0)) do
   	if(mod(n,i)==0) d=d+i+n/i
      i=i+1
   end while
   if(int(sqrt(n*1.0))-n==0) d=d-int(sqrt(n*1.0))
   end function