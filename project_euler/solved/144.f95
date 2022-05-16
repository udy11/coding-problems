! ALGEBRA and (pretty much) BRUTE FORCE

! Get the equation of reflected line
! given by y=r*x+c in the subroutine.
! Then get the points on the ellipse.

    implicit real*8(A-H,O-Z)
    x1=0.d0; y1=10.1d0
    x2=1.4d0; y2=-9.6d0
    nr=0
    write(6,*) x1,y1
    write(6,*) x2,y2
    do while(y2<9.99997999997999996d0)
        nr=nr+1
        call rflc(x1,y1,x2,y2)
        write(6,*) x2,y2
    enddo
    write(6,*) nr
    end

    subroutine rflc(x1,y1,x2,y2)
    implicit real*8(A-H,O-Z)
    x22=x2*x2
    x23=x22*x2
    y22=y2*y2
    y23=y22*y2
    t1=16.d0*x22*y1
    t2=8.d0*x2*y2*x1
    t3=8.d0*x22*y2
    t4=y1*y22
    d1=1.d0/(16.d0*x22*(x2-x1)-8.d0*x2*y1*y2+(x1+7.d0*x2)*y22)
    r=(t1-t2-t3-t4+y23)*d1
    c=((-t1-t2+3.d0*t3-7.d0*t4+6.d0*y23)*x2+x1*y23)*d1
    d2=4.d0+r*r
    t5=2.d0*sqrt(-c*c+25.d0*d2)
    x1=x2
    y1=y2
    x2=-(c*r+t5)/d2
    x3=(-c*r+t5)/d2
    if(abs(x2-x1)<1.d-10) then
        x2=x3
        y2=(4.d0*c+r*t5)/d2
    else
        y2=(4.d0*c-r*t5)/d2
    endif
    endsubroutine
