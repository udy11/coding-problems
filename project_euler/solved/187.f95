! SIEVE

! Someone on forums suggested this:
!   n=10^8;
!   Sum[If[PrimeQ[i],PrimePi[n/i]-PrimePi[i]+1,0],{i,2,Sqrt[n]}]
! It will be worth understanding the concept behind it

    implicit integer*8(I-N)
    dimension np(50000000),nd(100000000)
    integer nc(100000000)
    n=49999999
    call primes_soe_64(n,np,m)
    write(6,*) m,'primes generated'
    do j=1,100000000
        nd(j)=j
    enddo
    nc=0
    do i=1,m
        do j=np(i),100000000,np(i)
            nd(j)=nd(j)/np(i)
            nc(j)=nc(j)+1
        enddo
    enddo
    ns=0
    do i=1,100000000
        if(nd(i)==1 .and. nc(i)==2) ns=ns+1
    enddo
    write(6,*) ns+1229 ! 1229 to count all squares of primes
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
