    implicit integer*8(I-N)
    character*150 ofln
    n=1000000
    ofln="001.txt"
    call prm_ert_upto_n_fyl_64(n,ofln)
    end

! Subroutine (64-bit) to generate
! Prime Numbers using Sieves of Eratosthenes
! n is upto what primes are required (inclusive)
! ofln is output file
    subroutine prm_ert_upto_n_fyl_64(n,ofln)
    implicit integer*8(I-N)
    logical ip(n)
    dimension np(n)
    character*150 ofln
    ip(1)=.false.
    ip(2)=.true.
    do j=3,n,2
        ip(j)=.true.
        ip(j+1)=.false.
    enddo
    k=3
    nsq=int(sqrt(n*1.d0))+1
    do while(k<nsq)
        do j=k*k,n,k
            ip(j)=.false.
        enddo
        do while(k<nsq)
            k=k+2
            if(ip(k)) then
                exit
            endif
        enddo
    enddo
    open(144,file=ofln)
    write(144,*) 2
    do i=3,n,2
        if(ip(i)) then
            write(144,*) i
        endif
    enddo
    close(144)
    endsubroutine
