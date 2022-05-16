! SIEVE

    dimension nn(2:9999999)
    nn=1
    do i=2,4999999
        do j=i,9999999,i
            nn(j)=nn(j)+1
        enddo
    enddo
    nc=0
    do j=2,9999998
        if(nn(j)==nn(j+1)) nc=nc+1
    enddo
    write(6,*) nc
    end

