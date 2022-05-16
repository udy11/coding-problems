! ALGORITHM

! Basically generate all numbers of form 11..1
! in all bases until they cross 10^12

! Sorting is needed to remove repeated numbers

    implicit integer*8(I-N)
    dimension nsr(2000000)

    i=0
    k=3
    do
        m=0
        j=2
        do
            m=0
            do l=0,k-1
                m=m+j**l
            enddo
            if(m<1000000000000d0) then
                i=i+1
                nsr(i)=m
            else
                exit
            endif
            j=j+1
        enddo
        if(j==2) then
            exit
        else
            k=k+1
        endif
    enddo

    call merge_sort_asc_intg64(i,nsr)

    nsrsm=1
    j=1
    do while(j<=i)
        if(j<i .and. nsr(j)==nsr(j+1)) then
            j=j+1
            do while(j<i .and. nsr(j)==nsr(j+1))
                j=j+1
            enddo
        endif
        nsrsm=nsrsm+nsr(j)
        j=j+1
    enddo
    write(6,*) i,nsrsm

    end

! Merge Sort
    subroutine merge_sort_asc_intg64(n,na)
    implicit integer*8(I-N)
    logical sw
    dimension na(n),nb(n)
    if(n<2) return
    j=1
    nb(n)=na(n)
    do while(j<n)
        if(na(j)>na(j+1)) then
            nb(j)=na(j+1)
            nb(j+1)=na(j)
        else
            nb(j)=na(j)
            nb(j+1)=na(j+1)
        endif
        j=j+2
    enddo
    sw=.false.
    m=2
    do while(m<=n)
        if(sw) then
            i1=1
            do while(i1<=n)
                i2=i1+m
                if(i2>n) then
                    nb(i1:n)=na(i1:n)
                    exit
                endif
                if(i2+m-1>n) then
                    j0=n
                else
                    j0=i1+2*m-1
                endif
                j=i1
                i10=i1+m-1
                do while(j<=j0)
                    if(na(i1)<na(i2)) then
                        nb(j)=na(i1)
                        i1=i1+1
                    else
                        nb(j)=na(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        nb(j:j0)=na(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        nb(j:j0)=na(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.false.
            m=2*m
        else
            i1=1
            do while(i1<=n)
                i2=i1+m
                if(i2>n) then
                    na(i1:n)=nb(i1:n)
                    exit
                endif
                if(i2+m-1>n) then
                    j0=n
                else
                    j0=i1+2*m-1
                endif
                j=i1
                i10=i1+m-1
                do while(j<=j0)
                    if(nb(i1)<nb(i2)) then
                        na(j)=nb(i1)
                        i1=i1+1
                    else
                        na(j)=nb(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        na(j:j0)=nb(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        na(j:j0)=nb(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.true.
            m=2*m
        endif
    enddo
    if(.not. sw) na(1:n)=nb(1:n)
    endsubroutine
