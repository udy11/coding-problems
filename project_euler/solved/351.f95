! SIEVE

! Takes time but perhaps a better implementation
! can make it much more efficient

    implicit integer*8(I-N)
    n=100000000
    call H(n,nh)
    write(6,*) nh
    end

    subroutine H(n,nh)
    implicit integer*8(I-N)
    dimension np(n)
    do j=2,n
        np(j)=j-1
    enddo
    nw=0
    do j=2,n
        do i=2*j,n,j
            np(i)=np(i)-np(j)
        enddo
        nw=nw+np(j)
    enddo
    nh=6*(n-1+n*(n-1)/2-nw)
    endsubroutine
