! SIEVE

! Of course, problem is to find sum of totient
! function from 2 to 1000000
! For this, create an identity array, i.e. nq(i)=i
! Then for each prime below 1000001, change the array nq
! accordingly (sort of what we do in Sieves methods)
! Then nq array will contain all the Totient Function values
! Simply take sum of it

    implicit integer*8(I-N)
    dimension np(1000000),nq(1000000)
    n=1000000
    do i=1,n
        nq(i)=i
    enddo
    call primes_soe_64(n,np,m)
    do mp=1,m
        do nn=np(mp),n,np(mp)
            nq(nn)=nq(nn)*(np(mp)-1)
            nq(nn)=nq(nn)/np(mp)
        enddo
    enddo
    ns=1
    do i=3,n
        ns=ns+nq(i)
    enddo
    write(6,*) ns
    end

! Subroutine (64-bit) to generate
! Prime Numbers using the sieve of Eratosthenes
    subroutine primes_soe_64(n,np,m)
    implicit integer*8(I-N)
    logical ip((n-1)/2)
    dimension np(1+(n-1)/2)
    if(n<2) then
        m=0
        return
    endif
    ip=.true.
    n2=(n-1)/2
    k=3
    nsq=int(sqrt(n*1.d0)+0.5d0,8)
    do while(k<=nsq)
        do i=k*k/2,n2,k
            ip(i)=.false.
        enddo
        do while(k<=nsq)
            k=k+2
            if(ip(k/2)) then
                exit
            endif
        enddo
    enddo
    m=1
    np(1)=int(2,8)
    do i=1,n2
        if(ip(i)) then
            m=m+1
            np(m)=2*i+1
        endif
    enddo
    endsubroutine
