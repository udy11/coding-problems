	integer*8 c(20,20),max,p1,p2,p3,p4
    open(1,file='011_data.dat',status='old')
    do i=1,20
		read(1,*) (c(i,j),j=1,20)
    end do
    max=0
    do i=1,17
    	do j=1,20
			p1=1; p2=1; p3=1; p4=1
            do k=0,3
            	p1=p1*c(i+k,j)
                p2=p2*c(j,i+k)
                if(j<18) then
	                p3=p3*c(i+k,j+k)
                   p4=p4*c(i+k,21-j-k)
                end if
            end do
            if(p1>max) then
              max=p1
              ns=1
              i1=i; j1=j
            end if
            if(p2>max) then
              max=p2
              ns=2
              i1=i; j1=j
            end if
            if(p3>max) then
              max=p3
              ns=3
              i1=i; j1=j
            end if
            if(p4>max) then
              max=p4
              ns=4
              i1=i; j1=21-j
            end if
       end do
   end do
   print *,max,ns,i1,j1
   end