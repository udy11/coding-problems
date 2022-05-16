! MATH

! If one wants to cover a square hole of side m
! and has maximum d tiles, one can do it in
! int(0.5*(-m+sqrt(m*m+d))) ways

    implicit integer*8(I-N)
    implicit real*8(A-H,O-Z)

    d=1000000.d0
    ns=0
    do m=1,int(d/4.d0)
        ns=ns+int(0.5d0*(-m+sqrt(m*m+d)),4)
    enddo

    write(6,*) ns

    end
