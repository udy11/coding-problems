! LAGRANGE INTERPOLATION POLYNOMIAL

! I feel implementation is not that good.. but anyway
! it gives the answer pretty quickly

    implicit real*8(A-H,O-Z)
    implicit integer*8(I-N)
    integer*8 u
    dimension ny(20)
    do i=1,20
        ny(i)=u(i)
    enddo
    s=0
    do i=1,10
        b=bop(i+1,ny)
        write(6,*) i,b
        s=s+b
    enddo
    write(6,*) 'Sum:',s
    end

    integer*8 function u(n)
    implicit integer*8(I-N)
!    u=n**3
    u=(1-n)*(1+n*n+n**4+n**6+n**8)+n**10
    endfunction

    real*8 function bop(nx,ny)
    implicit integer*8(I-N)
    implicit real*8(A-H,O-Z)
    dimension ny(nx-1)
    do i=1,nx-1
        z=1
        do j=1,nx-1
            if(i/=j) z=z*(1.d0*nx-j)/(1.d0*i-j)
        enddo
        bop=bop+ny(i)*z
    enddo
    endfunction
