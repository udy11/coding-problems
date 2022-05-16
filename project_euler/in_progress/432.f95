! UNSOLVED

! Method so-far is similar to 72 and gives
! correct answer for given example in problem
! but something completely different needs to be
! thought because even storing an array of 10^11
! 8-byte integers needs ~750GB space

    implicit integer*8(I-N)
    dimension np(1000000),nq(1000000)
    n=1000000
    do i=1,n
        nq(i)=i
    enddo
    write(6,*) "nq initialized"
    call prm_ert_upto_n_ary_64(n,np,m)
    write(6,*) "primes generated"
    do mp=8,m                      ! Due to 510510
        do nn=np(mp),n,np(mp)
            nq(nn)=nq(nn)*(np(mp)-1)
            nq(nn)=nq(nn)/np(mp)
        enddo
    enddo
    write(6,*) "sieving done"
    ns=0
    do i=1,n
        ns=ns+nq(i)
    enddo
    write(6,*) ns*92160            ! Due to 510510
    end

! Subroutine (64-bit) to generate
! Prime Numbers using Sieves of Eratosthenes
! n is upto what primes are required (inclusive)
! np is array which stores the primes
! m is how many primes were generated
    subroutine prm_ert_upto_n_ary_64(n,np,m)
    implicit integer*8(I-N)
    logical ip(n)
    dimension np(n)
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
    m=2
    np(1)=2
    do i=3,n,2
        if(ip(i)) then
            np(m)=i
            m=m+1
        endif
    enddo
    m=m-1
    endsubroutine
