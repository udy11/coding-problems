! CALCULUS

! Works pretty slowly, but mainly because of 128-bit precision
! and slow converging methods used

! Idea is to evaluate the volume of wasted space.
! To get that convert the equation of "big" cone
! to cylindrical coordinates, then integrate
! it to get the volume of that cone and subtract it
! with the corresponding cylinder's volume

! Calculation of volume can be made via Simpson's 1/3rd rule
! Then one can notice that wasted volumes can only contain squares
! of 20 to 25 only.
! So simply apply a root-finding method to get the value of x (c in program).
! I used Bisection Method, as it's most ensuring, but applying another
! method could have been much faster

    implicit real*16(A-H,O-Z)
    implicit integer*16(I-N)
    dimension a(6),b(6)
    common r,rl,hl,c,alf,ii
    pi=3.1415926535897932384626433832795028842q0
    r=6.0q0
    alf=0.87266462599716478846184538424430635672q0

    a(1)=1.6q0; b(1)=1.61q0
    a(2)=2.805q0; b(2)=2.807q0
    a(3)=3.67q0; b(3)=3.68q0
    a(4)=4.425q0; b(4)=4.43q0
    a(5)=5.105q0; b(5)=5.115q0
    a(6)=5.755q0; b(6)=5.76q0

    sx=0.0
    do i=1,6
        ii=i+19
        a0=a(i); b0=b(i)
        er=1.0q-16
        call bsctn_128(a0,b0,er)
        write(6,*) ii,c
        sx=sx+c
    enddo
    write(6,*) "Sum:",sx
    end

    real*16 function vr()
    implicit real*16(A-H,O-Z)
    implicit integer*16(I-N)
    common r,rl,hl,c,alf,ii
    pi=3.1415926535897932384626433832795028842q0
    a=0.0q0; b=2.0q0*pi; n=100000
    call int_smpsn_128(a,b,n,sm)
    vr = pi*r*r*hl - sm - ii*ii*1.0q0
    endfunction

    real*16 function fx(t)
    implicit real*16(A-H,O-Z)
    implicit integer*16(I-N)
    common r,rl,hl,c,alf,ii
    c2=c*c
    r2=r*r
    ct=cos(t); ct2=ct*ct; c2t=2.q0*ct2-1.0q0
    st=sin(t)
    cst=c*st
    rcst=r-cst
    cr=r2+c2-2.q0*r*cst
    scr=sqrt(cr)
    if(st==1.0q0) then
        fx=0.0q0
    else
        fx=c2*c*ct2*st*log((rcst+scr)/(c-cst))
    endif
    fx=fx+scr*(cr+3.q0*(r2+c2*c2t))/6.0q0
    fx=fx-c2*c*(1.0q0+3.q0*c2t)/6.0q0
    fx=hl*0.5q0*(r2-fx/rl)
    endfunction

    subroutine int_smpsn_128(a,b,n,sm)
    implicit real*16(A-H,O-Z)
    implicit integer*16(I-N)
    h=(b-a)/n
    sm=h*(fx(a)+fx(b))*0.333333333333333333333333333333333333q0
    do i=1,n/2
        sm=sm+h*(4.0q0*fx(a+(2.0q0*i-1.0q0)*h)+2.0q0*fx(a+2.0q0*i*h))*0.333333333333333333333333333333333333q0
    end do
    if(mod(n,2)==0) sm=sm-2.0q0*h*fx(b)*0.333333333333333333333333333333333333q0
    end

    subroutine bsctn_128(a0,b0,er)
    implicit real*16(A-H,O-Z)
    common r,rl,hl,c,alf,ii
    a=a0; b=b0
    c=a; rl=r+c; hl=rl/tan(alf)
    do
      c=a; rl=r+c; hl=rl/tan(alf)
      ya=vr()
      c=0.5q0*(a+b); rl=r+c; hl=rl/tan(alf)
      yc=vr()
      if(abs(yc)<er) then
        exit
      else if(ya*yc<0) then
        b=c
      else
        a=c
      endif
!      write(6,*) c,vr()
    enddo
    endsubroutine
