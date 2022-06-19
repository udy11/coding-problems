! IDEA
! All such triangles can be (a, a, a-1) or (a, a, a+1)
! Their area would be integral if (3a-1)(a+1) and (3a+1)(a-1) are squares respectively

    implicit real*8(A-H,O-Z)
    implicit integer*8(I-N)
    logical is_sqrn
    ns=0
    write(6,*) 'With sides: a, a, a-1'
    do i=3,333333333,2
        np=3*i-1
        if(is_sqrn(np*(i+1))) then
            ns=ns+np
            write(6,*) i,i,i-1
        endif
    enddo
    write(6,*)
    write(6,*) 'With sides: a, a, a+1'
    do i=3,333333333,2
        np=3*i+1
        if(is_sqrn(np*(i-1))) then
            ns=ns+np
            write(6,*) i,i,i+1
        endif
    enddo
    write(6,*) 
    write(6,*) 'Sum of Perimeters:',ns
    end

    logical function is_sqrn(n)
    implicit integer*8(I-N)
    n1=int((sqrt(n*1.d0))+0.5d0)
    if(n1*n1==n) then
        is_sqrn=.true.
    else
        is_sqrn=.false.
    endif
    endfunction
