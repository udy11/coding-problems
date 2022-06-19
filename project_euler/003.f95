	integer*8 i,m,j
    j=600851475142
	do i=1,j
    	if(mod(j+1,i)==0) m=i
    end do
    print *,m
    end
