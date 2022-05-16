	integer*8 t,d,rt1,rt2,l,y,q
	d=2; t=1; l=1; rt2=1; rt1=0
	do
	do i=1,4
	t=t+d
	y=1; q=2
   while(q<=sqrt(t*1.0)) do
		if(mod(t,q)==0) then
		y=0
		exit
		end if
		q=q+1
	end while

	if(y==1) rt1=rt1+1
	end do
   rt2=rt2+4
   l=l+2
   if(rt1*1.0/rt2<0.1) exit
	d=d+2
	end do
	print *,l,rt1,rt2
	end