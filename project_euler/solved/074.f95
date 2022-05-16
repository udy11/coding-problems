! BRUTE-FORCE

! Many improvements can be made e.g. by storing the chains
! or storing the result of ns(), but this also works pretty fast

    implicit integer*8(I-N)
    dimension nf(0:9),np(61)
    common nf
    logical chk

! Storing Factorials
    nf(0)=1
    do i=1,9
        nf(i)=nf(i-1)*i
    enddo

    do n=1,1000000
        chk=.false.
        nn=n
        do k=1,61
            np(k)=ns(nn)
            do j=1,k-1
                if(np(k)==np(j)) then
                    chk=.true.
                    exit
                endif
            enddo
            if(chk) exit
            nn=np(k)
        enddo
        if(k==60) then
            nc=nc+1
        endif
    enddo
    write(6,*) nc

    end

    integer*8 function ns(n)
    implicit integer*8(I-N)
    dimension nf(0:9),nd(100)
    common nf
    l=len_int(n)
    call to_dgt(n,nd,l)
    ns=0
    do i=1,l
        ns=ns+nf(nd(i))
    enddo
    endfunction

    subroutine to_dgt(n,nd,m)
    implicit integer*8(I-N)
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

    integer*8 function len_int(n)
    implicit integer*8(I-N)
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
