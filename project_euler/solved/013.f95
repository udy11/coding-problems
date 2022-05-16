	integer c(100,50),r(10),s,t
	open(1,file='013_data.txt',status='old')
	do i=1,100
    	read(1,*) (c(i,j),j=1,50)
	end do
    t=0
    do j=50,1,-1
    	s=t
        do i=1,100
        	s=s+c(i,j)
        end do
        t=s/10
        print *,s
    end do
    end