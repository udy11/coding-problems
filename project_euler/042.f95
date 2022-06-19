	character*14 c(1786)
   integer t(20)
   open(1,file='42_words_1786.txt')

   do k=1,20
   	t(k)=k*(k+1)/2
   end do

   do i=1,1786
		read(1,*) c(i)
   end do

	n=0
	do j=1,1786
   s=0
	do i=1,14
   	if(c(j)(i:i)/=' ') s=s+(IACHAR(c(j)(i:i))-64)
      if(j==3) print *,c(j)(i:i),IACHAR(c(j)(i:i))-64
   end do
   do k=1,20
   	if(s==t(k)) then
	      n=n+1
	      exit
      end if
   end do
   end do

   print *,n
   end