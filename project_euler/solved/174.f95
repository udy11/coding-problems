! SIEVE

! Given number of tiles = d, the number of coverings k and
! side m of hole square are related as:
! 4*k*(m+k)=d
! So, with proper limits of k and m, just sieve and count
! how many d you get

! Code can further be optimized by further restricting limits of
! m and k than what I have chosen

    implicit integer*8(I-N)
    dimension nn(1000000)

    nd=1000000
    nn=0

    do m=1,nd/4
        do k=1,500
            j=4*k*(k+m)
            if(j<=nd) nn(j)=nn(j)+1
        enddo
    enddo

    nc=0
    do j=1,1000000
        if(nn(j)<11 .and. nn(j)>0) nc=nc+1
    enddo

    write(6,*) nc

    end
