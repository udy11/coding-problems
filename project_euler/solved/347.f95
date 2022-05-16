! BRUTE-FORCE (pretty much, and optimized)

! Simply generate required primes, then
! couple the possible primes and
! calculate M(p,q,N)

! One can think of sieving also, not
! sure if it will work though

    implicit integer*8(I-N)
    dimension np(350000)
    n2=10000000
    n=n2/2
    call primes_soe_64(n,np,m)

    j1=1
    ms=0
    do i=m,1,-1
        j1=nbsan_asc_64(np,j1,i,1.d0*n2/np(i))
        do j=1,j1
            if(j/=i) then
                call getmm(np(i),np(j),n2,mm)
                ms=ms+mm
            endif
        enddo
    enddo
    
    write(6,*) ms

    end

! To get M(i,j,n)
    subroutine getmm(i,j,n,mm)
    implicit integer*8(I-N)
    real*8 a
    a=n*1.d0/(i*j)
    alg=log(a)
    mm=0
    ni=int(alg/log(i*1.d0))+1
    nj=int(alg/log(j*1.d0))+1
    do ki=1,ni
        ik=i**ki
        do kj=1,nj
            mt=ik*(j**kj)
            if(mt<=n .and. mt>mm) mm=mt
        enddo
    enddo
    endsubroutine

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

! To search nearest lower prime in array a of primes
    integer*8 function nbsan_asc_64(a,nn1,nn2,b)
    implicit integer*8(I-N)
    integer*8 a
    real*8 b,d1,d2
    dimension a(nn2)
    if(b>a(nn2)) then
        nbsan_asc_64=nn2
        return
    endif
    if(b<a(nn1)) then
        nbsan_asc_64=nn1
        return
    endif
    n1=nn1; n2=nn2
    nd=n2-n1
    nm=n1+nd/2
    do while(nd>1)
        if(a(nm)>b) then
            n2=nm
        else
            n1=nm
        endif
        nd=n2-n1
        nm=n1+nd/2
    enddo
    d1=b-a(n1)
    d2=a(n2)-b
    if(d2==0.d0) then
        nbsan_asc_64=n2
    else
        nbsan_asc_64=n1
    endif
    endfunction
