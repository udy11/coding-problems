	do i=1,500
    	a=(1000000-2000.0*i)/(2000-2.0*i)
        if(a-int(a)==0) print *,a,i
    end do
    end