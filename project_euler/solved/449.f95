! PARALLEL CURVE AND REVOLUTION OF SURFACE

! Main point to observe is the x-y symmetry of the problem
! With that we can assume that surface of chocolate will also
! be symmetric in x-y axes

! The parallel curve (to an ellipse) is given as (with b=1):
! x(t) = (a + 1/sqrt(a*a*sin(t)**2 + cos(t)**2)) * cos(t)
! y(t) = (1 + a/sqrt(a*a*sin(t)**2 + cos(t)**2)) * sin(t)

! The volume of surface of revolution is given as:
! Vol = 2 * Integrate[pi*x(t)*x(t)*dy(t)/dt, (t,0,pi/2)]
! This gives the total volume of candy + chocolate

    implicit real*8(A-H,O-Z)
    implicit integer*8(I-N)
    common a1,a2,pi

    pi=3.1415926535897932d0
    a=0.0d0; b=pi*0.5d0; n=100000
    a1=3.0d0; a2=a1*a1

    call int_smpsn_64(a,b,n,sm)
    write(6,*) 2.d0*sm-4.d0*a2*pi/3.d0
    end

! INPUT FUNCTION
    real*8 function fx(t)
    implicit real*8(A-H,O-Z)
    implicit integer*8(I-N)
    common a1,a2,pi
    x = (a1 + 1/sqrt(a2 * sin(t)**2 + cos(t)**2)) * cos(t)
    dy = (1 + sqrt(8.d0)*a1/((1+a2)-(a2-1)*cos(2.d0*t))**1.5d0) * cos(t)
    fx=pi*x*x*dy
    end function

! Simpson's 1/3rd Rule Subroutine (64-bit)
    subroutine int_smpsn_64(a,b,n,sm)
    implicit real*8(A-H,O-Z)
    implicit integer*8(I-N)
    h=(b-a)/n
    sm=h*(fx(a)+fx(b))*0.333333333333333333d0
    do i=1,n/2
        sm=sm+h*(4.0d0*fx(a+(2.0d0*i-1.0d0)*h)+2.0d0*fx(a+2.0d0*i*h))*0.333333333333333333d0
    end do
    if(mod(n,2)==0) sm=sm-2.0d0*h*fx(b)*0.333333333333333333d0
    end
