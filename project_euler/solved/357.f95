! SIEVE

! Things can be improved by properly selecting the range of
! binary search.
! Another improvement can be made by changing limit of i
! in main loop, for example, for number 10, we only
! need to check divisors 1 and 2 and we need not check
! 5 and 10.

    implicit integer*8(I-N)
    logical di(100000000)
    dimension np(100000000)
    n1=1
    n=100000000
    di=.true.
    call primes_soe_64(n+1,np,mp)
    do i=1,n
        do j=i,n,i
            if(di(j)) then
                if(nbsa_asc_64(np,n1,mp,i+j/i)<0) then
                    di(j)=.false.
                endif
            endif
        enddo
    enddo
    ns=0
    do i=1,n
        if(di(i)) then
            ns=ns+i
            !write(6,*) i
        endif
    enddo
    write(6,*) 'Sum:',ns
    end

    integer*8 function nbsa_asc_64(a,nn1,nn2,b)
    implicit integer*8(I-N)
    integer*8 a,b
    dimension a(nn2)
    if(b>a(nn2)) then
        nbsa_asc_64=-1  ! Not Found
        return
    endif
    if(b<a(nn1)) then
        nbsa_asc_64=-1  ! Not Found
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
    if(a(n1)==b) then
        nbsa_asc_64=n1
    else if(a(n2)==b) then
        nbsa_asc_64=n2
    else
        nbsa_asc_64=-1  ! Not Found
    endif
    endfunction

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
