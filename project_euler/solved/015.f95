	integer*8 s,p(22,22)

	n=3
	do k=1,n+1
	p(k,1)=1
	p(1,k)=1
	end do
	do s=3,2*n+2
	do i=1,s-1
	j=s-i
	if(i>1 .and. j>1 .and. i<=n+1 .and. j<=n+1) then
	p(i,j)=p(i-1,j)+p(i,j-1)
	print *,i,j,p(i,j)
	end if
	end do
	end do
	print *,p(n+1,n+1)
	end