	integer p,s,n(100,2),q,r
    dimension p(-1:162),s(-1:162)
    do i=-1,162
    	p(i)=0; s(i)=0
    end do
    p(1)=1; s(1)=p(1)
	do i=0,9
    do j=1,10
    	n(10*i+j,1)=mod(j,10)
    	n(10*i+j,2)=(10*i+j)/10
    end do
    end do

	do i=2,99
		r=0
	do j=1,160
		q=r
	do k=1,2
		q=q+n(i,k)*p(j-k+1)
    end do
	s(j)=mod(q,10)
	r=q/10
    end do
	do m=-1,162
		p(m)=s(m)
	end do
	end do

	sm=0
	do k=1,160
		sm=sm+p(k)
	end do
   print *,sm

    end