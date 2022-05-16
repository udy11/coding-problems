! DYNAMIC PROGRAMMING (perhaps...)

! Store all interior points for possible lines in one
! quadrant. Rest is straightforward.

! I think much better strategy and implementation are possible.

    integer x,y
    logical is_sqrn
    dimension ilp(100,100)
    
    n=100
    ilp=0
    do i=1,n
        do j=1,i
            do y=1,j-1
                x=-y*i/j+i-1
                ilp(i,j)=ilp(i,j)+x
            enddo
        enddo
    enddo
    
    do i=1,n
        do j=1,i-1
            ilp(j,i)=ilp(i,j)
        enddo
    enddo

    nv=0
    do i1=1,n
        do j1=1,n
            do i2=1,n
                do j2=1,n
                    nqs=ilp(i1,j1)+ilp(j1,i2)+ilp(i2,j2)+ilp(j2,i1)
                    nqs=nqs+i1+j1+i2+j2-3
                    if(is_sqrn(nqs)) nv=nv+1
                enddo
            enddo
        enddo
    enddo
    
    write(6,*) nv

    end

    logical function is_sqrn(n)
    integer n,r
    if(mod(n,4)==0 .or. mod(n,8)==1) then
        r=int(sqrt(1.d0*n)+0.5d0)
        if(r*r==n) then
            is_sqrn=.true.
        else
            is_sqrn=.false.
        endif
    else
        is_sqrn=.false.
    endif
    endfunction
