! BISECTION METHOD

! This arithmetic geometric series will have sum:
! a*(1-r**n)/(1-r)+b*((1-r**n)/(1-r)-n*r**n)/(1-r)
! If you fiddle a bit with numbers and see some plots
! of this around 1, you'll notice that root should lie
! between 1.001 and 1.003, rest is just bisection method...

    implicit real*16(A-H,O-Z)
    external f
    a0=1.001q0; b0=1.003q0
    er=4.q-20

    call bsctn_128(a0,b0,er,c,istt,f)
    write(6,*) c

    end

! Function whose root is to be found
    real*16 function f(r)
    implicit real*16(A-H,O-Z)
    rn=r**5.0q3
    f=9.q2*(1.q0-rn)/(1.q0-r)-3.q0*((1.q0-rn)/(1.q0-r)-5.q3*rn)/(1.q0-r)+6.q11
    endfunction

! Subroutine (128-bit) to find a root of f(x) using Bisection Method
    subroutine bsctn_128(a0,b0,er,c,istt,f)
    implicit real*16(A-H,O-Z)
    logical ifa
    external f
    fa=f(a0)
    if(abs(fa)<er) then
        c=a0
        istt=2
        return
    endif
    if(abs(f(b0))<er) then
        c=b0
        istt=3
        return
    endif
    a=a0; b=b0; ifa=.false.
    c=0.5q0*(a+b)
    if(c==0.q0) then
        c0=1.q0
    else
        c0=0.q0
    endif
    do
        fc=f(c)
        if(abs(fc)<er) then
            istt=1
            exit
        else if(c==c0) then
            istt=-1
            exit
        else
            if(ifa) fa=f(a)
            if(fa*fc<0) then
                b=c
                ifa=.false.
            else
                a=c
                ifa=.true.
            endif
        endif
        c0=c
        c=0.5q0*(a+b)
    enddo
    endsubroutine
