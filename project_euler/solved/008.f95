	integer c(1000)
	open(1,file='008_data.dat',status='old')
    read(1,*) (c(i),i=1,1000)
    max=1
    do i=1,996
    	p=1
		do j=0,4
        	p=p*c(j+i)
        end do
        if(p>=max) then
          max=p
          n=i
        end if
    end do
    print *,max,n
    print *,(c(k),k=n,n+4) 
    end