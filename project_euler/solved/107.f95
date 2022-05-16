! Prim's Algorithm

    integer a(100,100),b(100,100)

    n=40
    open(67,file='107_network.txt')
    do i=1,n
        read(67,*) (a(i,j),j=1,n)
    enddo

    call prim_intg32(n,a(1:n,1:n),b(1:n,1:n))

    write(6,*) sum(a)/2-sum(b)

    end

! Subroutine (32-bit) to solve minimum spanning tree problem
! using Prim's Algorithm with integer weights
    subroutine prim_intg32(n,a,b)
    integer a(n,n),b(n,n)
    logical vt(n),vg(n)
    b=0
    vt=.false.
    vg=.true.
    vg(1)=.false.
    vt(1)=.true.
    k=1
    imin=0
    jmin=0
    do while(k<n)
        minw=2147483647
        do i=1,n
            if(vt(i)) then
                do j=1,n
                    if(vg(j) .and. a(i,j)<minw .and. a(i,j)>0) then
                        minw=a(i,j)
                        imin=i
                        jmin=j
                    endif
                enddo
            endif
        enddo
        vt(jmin)=.true.
        vg(jmin)=.false.
        b(imin,jmin)=a(imin,jmin)
        k=k+1
    enddo
    endsubroutine
