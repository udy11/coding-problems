	integer*8 ab(10000),d,nm(28123),cs,s
	open(1,file='023_out.txt')

	do i=1,28123
		nm(i)=i
   end do

	n=1; j=1
   while(n<=28123) do
	if(d(n)>n) then
   	ab(j)=n
      write(1,*) j,ab(j)
      j=j+1
   end if
   n=n+1
   end while

	do i=1,j-1
		do l=1,j-1
      cs=ab(i)+ab(l)
      if(cs<28124) nm(cs)=0
		end do
   end do

	s=0
   do k=1,23123
		s=s+nm(k)
   end do
   print *,s

   end
   

	integer*8 function d(n)
   d=1; i=2
   while(i<=sqrt(n*1.0)) do
   	if(mod(n,i)==0) d=d+i+n/i
      i=i+1
   end while
   if(int(sqrt(n*1.0))-sqrt(1.0*n)==0) d=d-int(sqrt(n*1.0))
   end function