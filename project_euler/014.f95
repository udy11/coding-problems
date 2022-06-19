	integer*8 n,m
	max=0
	do i=2,999999
    c=1; n=i
    while(n/=1) do
        n=m(n)
        c=c+1
    end while
	if(c>max) then
    	max=c
        j=i
    end if
    end do
    print *,max,j
    end

	integer*8 function m(n)
    integer*8 m,n
    if(mod(n,2)==0) then
    	m=n/2
        else
        	m=3*n+1
    end if
    end function