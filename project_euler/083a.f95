! FAILED IDEA

! Idea was to keep on updating b,c,d...
! using a,b,c... respectively in:
! a b c d e
! b b c d e
! c c c d e
! d d d d e
! e e e e e
! However it will fail in matrices like:
! 1 1 1 1 1
! x x x x 1
! x 1 1 1 1
! x 1 x x x
! x 1 1 1 1
! May be with some improvements, it can be made better

    dimension m0(80,80),m1(80,80)
    dimension mp1(159,2),mp2(159,2),mi(2),mt(159,2),ii(2)
    open(83,file='083_matrix1.txt')
    n=10
    do i=1,n
        read(83,*) (m0(i,j),j=1,n)
    enddo
    m1=9999999
    m1(1,1)=m0(1,1)

    do mm=2,n
        call itc(mm,mt,nt)

        ! For horizontal indices
        do i=1,nt/2
            ii(1)=mt(i,1); ii(2)=mt(i,2)
            minsm=9999999

            ! Checking just above index
            ns=m0(ii(1),ii(2))+m0(ii(1)-1,ii(2))
            if(minsm>ns) minsm=ns

            call pths(ii,mp1,mp2,np1,np2)
            ! Checking left paths
            do j=1,np1
                j1=mp1(j,1); j2=mp1(j,2)
                ns=m0(j1-1,j2)+m0(ii(1),ii(2))
                do k=1,j
                    ns=ns+m0(mp1(k,1),mp1(k,2))
                enddo
                if(minsm>ns) minsm=ns
            enddo
            ! Checking right and above paths
            do j=1,np2
                j1=mp2(j,1); j2=mp2(j,2)
                if(j1>j2) then
                    ns=m0(j1-1,j2)+m0(ii(1),ii(2))
                    do k=1,j
                        ns=ns+m0(mp2(k,1),mp2(k,2))
                    enddo
                    if(minsm>ns) minsm=ns
                else if(j1+1<j2) then
                    ns=m0(j1,j2-1)+m0(ii(1),ii(2))
                    do k=1,j
                        ns=ns+m0(mp2(k,1),mp2(k,2))
                    enddo
                    if(minsm>ns) minsm=ns
                endif
            enddo
            if(minsm<m0(ii(1),ii(2))+m0(ii(1)+1,ii(2))) then
                m1(ii(1),ii(2))=minsm
            else
                m1(ii(1),ii(2))=m0(ii(1),ii(2))
            endif
        enddo

        ! For vertical indices
        do i=2+nt/2,nt
            ii(1)=mt(i,1); ii(2)=mt(i,2)
            minsm=9999999
  
            ! Checking just left of index
            ns=m0(ii(1),ii(2))+m0(ii(1),ii(2)-1)
            if(minsm>ns) minsm=ns

            call pths(ii,mp1,mp2,np1,np2)
            ! Checking above paths  
            do j=1,np1
                j1=mp1(j,1); j2=mp1(j,2)
                ns=m0(j1,j2-1)+m0(ii(1),ii(2))
                do k=1,j
                    ns=ns+m0(mp1(k,1),mp1(k,2))
                enddo
                if(minsm>ns) minsm=ns
            enddo
            ! Checking below and left paths
            do j=1,np2
                j1=mp2(j,1); j2=mp2(j,2)
                if(j1<j2) then
                    ns=m0(j1,j2-1)+m0(ii(1),ii(2))
                    do k=1,j
                        ns=ns+m0(mp2(k,1),mp2(k,2))
                    enddo
                    if(minsm>ns) minsm=ns
                else if(j1>j2+1) then
                    ns=m0(j1-1,j2)+m0(ii(1),ii(2))
                    do k=1,j
                        ns=ns+m0(mp2(k,1),mp2(k,2))
                    enddo
                    if(minsm>ns) minsm=ns
                endif
            enddo
            if(minsm<m0(ii(1),ii(2))+m0(ii(1),ii(2)+1)) then
                m1(ii(1),ii(2))=minsm
            else
                m1(ii(1),ii(2))=m0(ii(1),ii(2))
            endif
        enddo

        ! For equal indices
        i=1+nt/2
        ii(1)=mt(i,1); ii(2)=mt(i,2)
        minsm=9999999
        call pths(ii,mp1,mp2,np1,np2)
        ! Checking left paths
        do j=1,np1
            j1=mp1(j,1); j2=mp1(j,2)
            ns=m0(j1-1,j2)+m0(ii(1),ii(2))
            do k=1,j
                ns=ns+m0(mp1(k,1),mp1(k,2))
            enddo
            if(minsm>ns) minsm=ns
        enddo
        ! Checking above paths
        do j=1,np2
            j1=mp2(j,1); j2=mp2(j,2)
            ns=m0(j1,j2-1)+m0(ii(1),ii(2))
            do k=1,j
                ns=ns+m0(mp2(k,1),mp2(k,2))
            enddo
            if(minsm>ns) minsm=ns
        enddo
        if(minsm<m0(ii(1),ii(2))+m0(ii(1)+1,ii(2)) .and. minsm<m0(ii(1),ii(2))+m0(ii(1),ii(2)+1)) then
            m1(ii(1),ii(2))=minsm
        else
            m1(ii(1),ii(2))=m0(ii(1),ii(2))
        endif

        ! Resetting m0 matrix
        do i=1,nt
            m0(mt(i,1),mt(i,2))=m1(mt(i,1),mt(i,2))
        enddo
    enddo

    open(80,file='083_mm.txt')
    n=10
    do i=1,n
        write(80,*) (m0(i,j),j=1,n)
    enddo
    write(80,*)
    do i=1,n
        write(80,*) (m1(i,j),j=1,n)
    enddo
    close(80)
    end

    subroutine pths(mi,mp1,mp2,n1,n2)
    dimension mi(2),mp1(159,2),mp2(159,2)
    if(mi(1)>mi(2)) then
        n1=mi(2)-1
        k=1
        do i=mi(2)-1,1,-1
            mp1(k,1)=mi(1)
            mp1(k,2)=i
            k=k+1
        enddo
        n2=2*mi(1)-2-n1
        k=1
        do i=mi(2)+1,mi(1)-1
            mp2(k,1)=mi(1)
            mp2(k,2)=i
            k=k+1
        enddo
        do i=mi(1),1,-1
            mp2(k,1)=i
            mp2(k,2)=mi(1)
            k=k+1
        enddo
    else if(mi(1)<mi(2)) then
        n1=mi(1)-1
        k=1
        do i=mi(1)-1,1,-1
            mp1(k,1)=i
            mp1(k,2)=mi(2)
            k=k+1
        enddo
        n2=2*mi(2)-2-n1
        k=1
        do i=mi(1)+1,mi(2)-1
            mp2(k,1)=i
            mp2(k,2)=mi(2)
            k=k+1
        enddo
        do i=mi(2),1,-1
            mp2(k,1)=mi(2)
            mp2(k,2)=i
            k=k+1
        enddo
    else
        n1=mi(1)-1
        n2=n1
        k=1
        do i=n1,1,-1
            mp1(k,1)=mi(1)
            mp1(k,2)=i
            mp2(k,1)=i
            mp2(k,2)=mi(2)
            k=k+1
        enddo
    endif
    endsubroutine

    subroutine itc(n,mic,k)
    dimension mic(159,2)
    k=0
    do i=1,n
        k=k+1
        mic(k,1)=n
        mic(k,2)=i
    enddo
    do i=n-1,1,-1
        k=k+1
        mic(k,1)=i
        mic(k,2)=n
    enddo
    endsubroutine
