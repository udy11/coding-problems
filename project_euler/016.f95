	integer p,s,q,r
	dimension p(-1:307),s(-1:307)
	do i=-1,307
		p(i)=0; s(i)=0
	end do
	p(1)=1; s(1)=p(1)

	do i=1,1000
		r=0
	do j=1,305
		q=r+2*p(j)
		s(j)=mod(q,10)
		r=q/10
	end do
	do m=-1,307
		p(m)=s(m)
	end do
	end do

	sm=0
	do k=1,305
		sm=sm+p(k)
      print *,p(k)
	end do
   print *,sm

	end