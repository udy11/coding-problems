	integer*8 s,t,d
	s=1; d=2; t=1
	while (t<=1001*1001) do
	do i=1,4
	t=t+d
	s=s+t
   print *,sqrt(1.0*t),t,s
	end do
	d=d+2
	end while
	print *,s
	end