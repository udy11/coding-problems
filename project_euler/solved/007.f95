	i=2; k=3
	while(i<10002) do
    	y=1;
    	do j=2,k-1
        	if (mod(k,j)==0) y=0
        end do
        if (y==1) then
          p=k
          i=i+1
        end if
        k=k+1
    end while
    print *,p
    end