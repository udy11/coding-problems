! 4 points can tackle this problem quite efficiently:
! triangle numbers are n(n+1)/2 for all natural numbers n
! two consecutive natural numbers cannot have common divisors except 1
! while checking for total divisors of n, checking upto sqrt(n) will suffice
! however, if n is a perfect square, you will double count sqrt(n), so balance that

	integer d2,d1
	i=2
	do
		d1=2; d2=2
		i1=i
      i2=i+1
      if(mod(i1,2)==0) then
      	i1=i1/2
         else
           i2=i2/2
      end if
      j=2; k=2
      while(j<=sqrt(i1*1.0)) do
         if(mod(i1,j)==0) d1=d1+2
         j=j+1
		end while
		if(j==sqrt(i1*1.0)) d1=d1-1
		while(k<=sqrt(i2*1.0)) do
         if(mod(i2,k)==0) d2=d2+2
         k=k+1
		end while
		if(k==sqrt(i2*1.0)) d2=d2-1
		print *,i1,j,d1,i2,k,d2
		if(d2*d1>500) exit
		i=i+1
		if(mod(i,10000)==0) print *,i,' crossed'
	end do
	print *,i1*i2
	end