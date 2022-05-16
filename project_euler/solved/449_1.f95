! FAILED IDEA

! Idea was to fit the chocolate's surface with a
! surface (as given in subroutine fx), however,
! a much better guess is required, as it did not result
! into required accuracy

    implicit real*8(A-H,O-Z)
    dimension x0(10),xmin(10)
    common cc(20000,3),a1,a2,a4,k

    n=22
    k=0
    a1=2.d0
    a2=a1*a1
    a4=a2*a2

    open(44,file='449.dat')
    do i=0,n
        x=i*(a1/n)
        do j=0,n
            y=j*(a1/n)
            ef=(x*x+y*y)/a2
            if(ef<=1.d0) then
                z=sqrt(1-ef)
                s=sqrt(x*x/a4+y*y/a4+z*z)
                k=k+1
                cc(k,1)=x+x/(a2*s); cc(k,2)=y+y/(a2*s); cc(k,3)=z+z/s
                write(44,*) cc(k,1:3)
            endif
        enddo
    enddo
    close(44)

    x0(1)=0.91762001567133067D0
    x0(2)=8.2774055498281249D-002
    x0(3)=5.1003060369325115D-003
    x0(4)=1.5614796057162325D-004
    x0(5)=1.5614796057162325D-005

    eps=1.d-8

    call grad_desc(5,eps,x0,xmin,fmin)

    write(6,*)
    do i=1,5
        write(6,*) xmin(i)
    enddo
    write(6,*) 'Minima: ',fmin
    end

    subroutine fx(n,x,f)
    implicit real*8(A-H,O-Z)
    dimension x(n)
    common cc(20000,3),a1,a2,a4,k
    f=0.d0
    do i=1,k
        xx=cc(i,1)
        yy=cc(i,2)
        zz=cc(i,3)
!        ff=x(1)*a1*sqrt(1.d0-xx/(a1+1)-yy/(a1+1))
        ff=x(1)*a1*sqrt(1.d0-xx*xx/(a1+1)**2-yy*yy/(a1+1)**2)
        ff=ff+x(2)*a1*sqrt(1.d0-xx**3/(a1+1)**3-yy**3/(a1+1)**3)
        ff=ff+x(3)*a1*sqrt(1.d0-xx**4/(a1+1)**4-yy**4/(a1+1)**4)
        ff=ff+x(4)*a1*sqrt(1.d0-xx**5/(a1+1)**5-yy**5/(a1+1)**5)
        ff=ff+x(5)*a1*sqrt(1.d0-xx**6/(a1+1)**6-yy**6/(a1+1)**6)
        fz=ff-zz
        f=f+fz*fz
    enddo
    endsubroutine

    subroutine gx(n,x,g)
    implicit real*8(A-H,O-Z)
    dimension x(n),g(n)
    common cc(20000,3),a1,a2,a4,k
    g=0.d0
    do i=1,k
        xx=cc(i,1)
        yy=cc(i,2)
        zz=cc(i,3)
!        ff=x(1)*a1*sqrt(1.d0-xx/(a1+1)-yy/(a1+1))
        ff=x(1)*a1*sqrt(1.d0-xx*xx/(a1+1)**2-yy*yy/(a1+1)**2)
        ff=ff+x(2)*a1*sqrt(1.d0-xx**3/(a1+1)**3-yy**3/(a1+1)**3)
        ff=ff+x(3)*a1*sqrt(1.d0-xx**4/(a1+1)**4-yy**4/(a1+1)**4)
        ff=ff+x(4)*a1*sqrt(1.d0-xx**5/(a1+1)**5-yy**5/(a1+1)**5)
        ff=ff+x(5)*a1*sqrt(1.d0-xx**6/(a1+1)**6-yy**6/(a1+1)**6)
        fz=2.d0*(ff-zz)
!        g(1)=g(1)+fz*a1*sqrt(1.d0-xx/(a1+1)-yy/(a1+1))
        g(1)=g(1)+fz*a1*sqrt(1.d0-xx*xx/(a1+1)**2-yy*yy/(a1+1)**2)
        g(2)=g(2)+fz*a1*sqrt(1.d0-xx**3/(a1+1)**3-yy**3/(a1+1)**3)
        g(3)=g(3)+fz*a1*sqrt(1.d0-xx**4/(a1+1)**4-yy**4/(a1+1)**4)
        g(4)=g(4)+fz*a1*sqrt(1.d0-xx**5/(a1+1)**5-yy**5/(a1+1)**5)
        g(5)=g(5)+fz*a1*sqrt(1.d0-xx**6/(a1+1)**6-yy**6/(a1+1)**6)
    enddo
    endsubroutine

    subroutine grad_desc(n,eps,x0,xmin,fmin)
    implicit real*8(A-H,O-Z)
    dimension x0(n),xmin(n),g(n),a(n)
    xmin=x0
    gsum=eps+1.d0
    do mm=1,4000
!    do while(gsum>eps)
        call gx(n,xmin,g)
        call lnsrch(n,xmin,g,a)
        xmin=xmin-a*g
        gsum=sum(abs(g))
        if(mod(mm,500)==0) then
            call fx(n,xmin,f)
            write(6,*) f,gsum
!            read(*,*)
        endif
    enddo
    fmin=f
    endsubroutine

    subroutine lnsrch(n,x0,g,a)
    implicit real*8(A-H,O-Z)
    dimension x0(n),a(n),g(n),x(n)
    x=x0
    a=1.d0
    call fx(n,x0,f0)
    do i=1,n
        df=1.d0
        do
            a(i)=a(i)*0.96d0
            x(i)=x0(i)-a(i)*g(n)
            call fx(n,x,f)
            if(f<f0 .or. a(i)<1.d-10) exit
        enddo
    enddo
    endsubroutine
