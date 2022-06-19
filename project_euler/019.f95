	integer mxd(12),yr,dm,c
	data (mxd(i),i=1,12)/31,28,31,30,31,30,31,31,30,31,30,31/
	d=6; yr=1901; mnth=1; dt=6; dm=d; c=0
	while (d<36526) do
	d=d+7
   dm=dm+7
	if(mod(yr,4)==0) then
   	mxd(2)=29
      else
        mxd(2)=28
   end if
   if(dm>mxd(mnth)) then
		dm=mod(dm,mxd(mnth))
		mnth=mnth+1
		mnth=mod(mnth,12)
      if(mnth==0) mnth=12
      if(mnth==1) yr=yr+1
		if(dm==1) then
      	c=c+1
         print *,mnth,yr
      end if
   end if
   end while
   print *,c
   end