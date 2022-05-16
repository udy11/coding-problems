	integer*8 s
    integer y,n(2000000)
	s=0; l=2000000
	do i=1,l
		n(i)=i
	end do		
	do i=2,l
		if(n(i)/=0) then
        y=1
        do j=2,i-1
        	if (mod(i,j)==0) then
            y=0
            exit
            end if
        end do

        if (y==1) then
        do j=i+1,l
        	if(mod(n(j),n(i))==0) n(j)=0
        end do
        s=s+n(i)
        end if
        end if
        if(mod(i,l/100)==0) print *,i*100/l,'% completed & sum is ',s
	end do
    print *,'Finale:',s
    end