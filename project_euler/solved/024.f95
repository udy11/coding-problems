	integer*8 n,e,fct,m(10),i
	nm=4; e=9
   fct=1
   do i=1,nm
   	fct=fct*i
   end do
   do k=1,nm
   	m(k)=k-1
   end do
   do n=nm,2,-1
   do i=1,n
   	if(e<=fct/n*i) then
      tm=m(i)
      e=e-fct/n*(i-1)
      fct=fct/n
      do j=i,n-1
      	m(j)=m(j+1)
      end do
      m(n)=tm
      exit
      end if
   end do
   end do
   print *,(m(j),j=1,nm)
   end