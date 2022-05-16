! program is only for help, this won't give any answer

	integer n(50)
	open(1,file='79_keylog.txt')
   do i=1,50
   	read(1,*) n(i)
      if (mod(n(i),10)==2) print *,mod(n(i),100)/10
   end do

   end