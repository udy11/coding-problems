!    include "int_tools.f95"
    implicit real*16(A-H,O-Z)
    implicit integer*16(I-N)
    integer nnd,npsmd
    dimension np(2000),npsmd(100),nnd(200),nnm(100)
    n=190; ps=1.q0
    call prm_ert_upto_n_ary_128(n,np,mp)
    do i=1,mp
        ps=ps*sqrt(1.q0*np(i))
    enddo
    nps=int(ps,16)
    write(6,*) nps
    write(6,*)

11  format(100I1)
    open(5,file="266a.txt")
    do m=-500,500
        npsm=nps+m
        write(5,*) m,npsm
        call to_dgt(npsm,npsmd,37)
        call int_mul(npsmd,npsmd,37,37,nnd)
        write(5,11) nnd(74:1:-1)
        write(5,*)
    enddo
    close(5)

    open(4,file="266b.txt")
    nps=2323218950681478446587180516177954548q0
    do i=500000000,1000000000
        nn=nps-i
        nnq=1
        do k=1,mp
            if(mod(nn,np(k))==0) then
!                nnm(k)=1
                nn=nn/np(k)
                nnq=nnq*np(k)
                do
                    if(mod(nn,np(k))==0) then
!                        nnm(k)=nnm(k)+1
                        nn=nn/np(k)
                        nnq=nnq*np(k)
                    else
                        exit
                    endif
                enddo
                !write(4,*) np(k),nnm(k)
            endif
        enddo
        if(nps-i-nnq==0) then
            write(6,*) nps-i
        endif
    enddo
    close(4)
    end

    subroutine prm_ert_upto_n_ary_128(n,np,m)
    implicit integer*16(I-N)
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

! Subroutine to multiply two numbers stored in arrays
    subroutine int_mul(n1d,n2d,m1,m2,n12d)
    integer*16 to_int,nc,nn
    logical kd
    dimension n1d(m1),n2d(m2),n12d(m1+m2),ntd(0:9,m1+1),kd(0:9)
111 format(100I3)
    kd=.false.
    do i=1,m2
        kd(n2d(i))=.true.
    enddo
    ntd=0
    do i=0,9
        if(kd(i)) then
            do j=1,m1
                nn=ntd(i,j)+n1d(j)*i
                ntd(i,j)=mod(nn,10)
                ntd(i,j+1)=nn/10
            enddo
        endif
    enddo
    n12d=0
    do i=1,m2
        call int_sm(ntd(n2d(i),:),n12d,m1+1,m1+m2,i)
    enddo
    endsubroutine

! Supplementary subroutine for multiplication
! Adds two numbers with specified shift for first
    subroutine int_sm(n1d,n2d,m1,m2,ii)
    dimension n1d(m1),n2d(m2)
    do i=ii,ii+m1-1
        nn=n1d(i-ii+1)+n2d(i)
        n2d(i)=mod(nn,10)
        n2d(i+1)=n2d(i+1)+nn/10
    enddo
    do i=ii+m1,m2
        nn=n2d(i)
        n2d(i)=mod(nn,10)
        n2d(i+1)=n2d(i+1)+nn/10
    enddo
    endsubroutine

! Adds two integers with their digits stored in array
! (9,9,9,9)+(9,9,9) -> (8,9,9,0,1)
    subroutine int_add(n1d,n2d,m1,m2,n12d,m12)
    dimension n1d(m1),n2d(m2),n12d(1+max(m1,m2))
    n12d=0
    if(m1>m2) then
        do i=1,m2
            nn=n1d(i)+n2d(i)+n12d(i)
            n12d(i)=mod(nn,10)
            n12d(i+1)=nn/10
        enddo
        do i=m2+1,m1
            nn=n1d(i)+n12d(i)
            n12d(i)=mod(nn,10)
            n12d(i+1)=nn/10
        enddo
        if(n12d(m1+1)>0) then
            m12=m1+1
        else
            m12=m1
        endif
    else
        do i=1,m1
            nn=n1d(i)+n2d(i)+n12d(i)
            n12d(i)=mod(nn,10)
            n12d(i+1)=nn/10
        enddo
        do i=m1+1,m2
            nn=n2d(i)+n12d(i)
            n12d(i)=mod(nn,10)
            n12d(i+1)=nn/10
        enddo
        if(n12d(m2+1)>0) then
            m12=m2+1
        else
            m12=m2
        endif
    endif
    endsubroutine
    
! Returns integer from array of digits
! (9,3,0,1,0) -> 1039
    integer*16 function to_int(nd,m)
    dimension nd(m)
    integer*16 k
    to_int=nd(1)
    do i=1,m-1
        k=1
        do j=1,i
            k=k*10
        enddo
        to_int=to_int+nd(i+1)*k
    enddo
    endfunction

! Returns all digits of an integer as array of digits
! 1039,6 -> (9,3,0,1,0,0)
    subroutine to_dgt(n,nd,m)
    integer*16 n,n1,k
    dimension nd(m)
    n1=n
    do i=m-1,0,-1
        k=1
        do j=1,i
            k=k*10
        enddo
        nd(i+1)=n1/k
        n1=n1-nd(i+1)*k
    enddo
    endsubroutine

! Returns length of integer
! 0 -> 1
! 47911 -> 5
    integer function len_int(n)
    integer*16 n,i,m
    if(n<10) then
        len_int=1
        return
    endif
    len_int=-1
    i=1
    do while(i>0)
        len_int=len_int+1
        m=1
        do j=1,len_int
            m=m*10
        enddo
        i=n/m
    enddo
    endfunction
