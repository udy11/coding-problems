	integer*8 p(1000000),y,z,s
    n=1000000
	p(1)=2; p(2)=3; k=2
    do i=4,n
    	y=1; j=1
        while(p(j)<=sqrt(i*1.0)) do
        	if(mod(i,p(j))==0) then
            y=0
            exit
            end if
            j=j+1
        end while
        if(y==1) then
        	k=k+1
            p(k)=i
        end if
    end do
	print *,k
    
	sum=0; k1=0
    while(sum<1000000) do
		k1=k1+1
    	sum=sum+p(k1)
    end while
    sum=sum-p(k1)
    k1=k1-1
    print *,k1,sum

	open(1,file='50_out.dat',status='replace')
	do m=k1,21,-1
    do i=1,k1-m+1
    	s=0
    	do j=i,m+i-1
			s=s+p(j)
        end do
        if(s<1000000) then
        l=1; z=1
        while(p(l)<=sqrt(s*1.0)) do
        	if(mod(s,p(l))==0) then
            z=0
            exit
            end if
            l=l+1
        end while
        if (z==1) write(1,*) m,i,s
        end if
	end do
!    if(z==1) exit
    end do
    print *,s
    end