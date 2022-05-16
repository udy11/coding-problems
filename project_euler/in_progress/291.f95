	integer*8 s,c
	c=0; w=1
	do
    do
       	t=(y/x)**3
    	s=(x-t*y)/(1+t)
        if (s>0 .and. s-int(s)==0) then
	        l=1; z=1
        	while(p(l)<=sqrt(s*1.0)) do
    	   	if(mod(s,p(l))==0) then
            z=0
           	exit
	        end if
	        l=l+1
		    end while
		end if
        if (s>=5000000000000000) then
        	w=0
            exit
        end if
        if(z==1) c=c+1
    end do
    if(w==0) exit
    end do
    print *,c
    end