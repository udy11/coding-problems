! this method is scum, i'll think of something better

	integer c(20,20),p(27)
   open(1,file='011_data.dat',status='old')
   do i=1,20
		read(1,*) (c(i,j),j=1,20)
   end do
    max=0
    do i=1,17
    	do j=1,17
			pr=c(i,j)
         p(1)=pr*c(i,j+1)*c(i,j+2)*c(i,j+3)
         p(2)=pr*c(i,j+1)*c(i,j+2)*c(i+1,j+3)
         p(3)=pr*c(i,j+1)*c(i,j+2)*c(i+1,j+2)
         p(4)=pr*c(i,j+1)*c(i+1,j+2)*c(i+1,j+3)
			p(5)=pr*c(i,j+1)*c(i+1,j+2)*c(i+2,j+3)
			p(6)=pr*c(i,j+1)*c(i+1,j+2)*c(i+2,j+2)
         p(7)=pr*c(i,j+1)*c(i+1,j+1)*c(i+1,j+2)
         p(8)=pr*c(i,j+1)*c(i+1,j+1)*c(i+2,j+2)
         p(9)=pr*c(i,j+1)*c(i+1,j+1)*c(i+2,j+1)
         p(10)=pr*c(i+1,j+1)*c(i+1,j+2)*c(i+1,j+3)
         p(11)=pr*c(i+1,j+1)*c(i+1,j+2)*c(i+2,j+3)
         p(12)=pr*c(i+1,j+1)*c(i+1,j+2)*c(i+2,j+2)
         p(13)=pr*c(i+1,j+1)*c(i+2,j+2)*c(i+2,j+3)
         p(14)=pr*c(i+1,j+1)*c(i+2,j+2)*c(i+3,j+3)
         p(15)=pr*c(i+1,j+1)*c(i+2,j+2)*c(i+3,j+2)
         p(16)=pr*c(i+1,j+1)*c(i+2,j+1)*c(i+2,j+2)
         p(17)=pr*c(i+1,j+1)*c(i+2,j+1)*c(i+3,j+2)
         p(18)=pr*c(i+1,j+1)*c(i+2,j+1)*c(i+3,j+1)
         p(19)=pr*c(i+1,j)*c(i+1,j+1)*c(i+1,j+2)
         p(20)=pr*c(i+1,j)*c(i+1,j+1)*c(i+2,j+2)
         p(21)=pr*c(i+1,j)*c(i+1,j+1)*c(i+2,j+1)
         p(22)=pr*c(i+1,j)*c(i+2,j+1)*c(i+2,j+2)
         p(23)=pr*c(i+1,j)*c(i+2,j+1)*c(i+3,j+2)
         p(24)=pr*c(i+1,j)*c(i+2,j+1)*c(i+3,j+1)
         p(25)=pr*c(i+1,j)*c(i+2,j)*c(i+2,j+1)
         p(26)=pr*c(i+1,j)*c(i+2,j)*c(i+3,j+1)
         p(27)=pr*c(i+1,j)*c(i+2,j)*c(i+3,j)

			do k=1,27
         if(p(k)>max) then
         	max=p(k)
         	print *,max
         end if
         end do

		end do
	end do
   print *,max
   end