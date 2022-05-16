! TRANSFER MATRIX METHOD and BRUTE-FORCE

! Transfer Matrix Method works to find between which 10^n and 10^(n+1)
! the answer lies. After which I begin the brute-force.

! One optimization can be in deciding bouncy numbers. For example,
! if it is found that 12100 is bouncy, then all 100 numbers 12100-12199
! will be bouncy.

    implicit integer*8(I-N)
    implicit real*8(A-H,O-Z)
    dimension mi(10,10),md(10,10),ni(10)
    dimension nd(10),kd(7)
    logical ib
    
    mi=0; ni=1; ni(1)=0
    md=0; nd=1; nd(1)=0
    do i=1,10
        do j=1,10
            if(i>=j) mi(i,j)=1
            if(i<=j) md(i,j)=1
        enddo
    enddo
    
    r0=0.99d0
    nb=0
    do k=2,8
        ni=matmul(mi,ni)
        nd=matmul(md,nd)
        nb=nb+9*10**(k-1)-(sum(ni)+sum(nd)-9)
        r=nb/(10.d0**k-1.d0)
        if(r>r0) exit
        nb0=nb
    enddo

    nt=10**(k-1)-1
    r=nb0/(1.d0*nt)
    do while(r<=r0)
        nt=nt+1
        call ifbnc(k,nt,ib)
        if(ib) then
            nb0=nb0+1
            r=nb0/(1.d0*nt)
        endif
    enddo
    write(6,*) nt-1
    end

! to check if the number is bouncy
    subroutine ifbnc(k,ii,ib)
    implicit integer*8(I-N)
    logical ib,ci,cd
    dimension id(k)
    call tdgs(k,ii,id)
    j=1
    do while(j<k)
        if(id(j)<id(j+1)) exit
        j=j+1
    enddo
    if(j==k) then
        ib=.false.
        return
    endif
    j=1
    do while(j<k)
        if(id(j)>id(j+1)) exit
        j=j+1
    enddo
    if(j==k) then
        ib=.false.
        return
    endif
    ib=.true.
    endsubroutine

! to get the digits of a number
    subroutine tdgs(k,ii,nd)
    implicit integer*8(I-N)
    dimension nd(k)
    m=ii
    do i=k-1,1,-1
        nd(i+1)=m/10**i
        m=m-nd(i+1)*10**i
    enddo
    nd(1)=m
    endsubroutine
