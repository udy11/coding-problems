	integer s
	s=2
    i0=1; i1=2; i2=0
    while(i2<=4000000) do
    i2=i1+i0
    i0=i1
    i1=i2
    if(mod(i2,2)==0) then
    	s=s+i2
!        print *,i2
    end if
    end while
1	format(I30.20)
	write(*,1) s
    end
