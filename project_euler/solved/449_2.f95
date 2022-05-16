! FAILED IDEA

! Idea was to integrate directly by generating the points
! Integration is performed in spherical coordinates.
! However, it did not result into required accuracy.

    implicit real*8(A-H,O-Z)
    dimension chc(0:9100,0:9100,3)
    common a1,ai2

    n=9100
    a1=2.d0

    ai2=1.d0/(a1*a1)
    pi=3.1415926535897932d0

    do i=0,n
        phi=i*pi*0.5d0/n
        r=1.d0/sqrt(ai2*sin(phi)**2+cos(phi)**2)
        do j=0,n
            tht=j*pi*0.5d0/n
            chc(i,j,1)=r*sin(phi)*cos(tht)
            chc(i,j,2)=r*sin(phi)*sin(tht)
            call fx(chc(i,j,1),chc(i,j,2),chc(i,j,3))
        enddo
    enddo

    cndy=0.d0
    do i=0,n-1
        do j=0,n-1
            call tri_vol(chc(i,j,:),chc(i+1,j,:),chc(i,j+1,:),vol)
            cndy=cndy+vol
            call tri_vol(chc(i+1,j+1,:),chc(i+1,j,:),chc(i,j+1,:),vol)
            cndy=cndy+vol
        enddo
    enddo

    write(6,*) 8.d0*cndy-4.d0*pi*a1*a1/3.d0
    end

    subroutine fx(x,y,z)
    implicit real*8(A-H,O-Z)
    common a1,ai2
    ef=(x*x+y*y)*ai2
    if(ef<=1.d0) then
        z=1-ef
        si=1.d0/sqrt(ef*ai2+z)
        z=sqrt(z)*(1.d0+si)
        x=x*(1.d0+si*ai2)
        y=y*(1.d0+si*ai2)
    else
        z=0.d0
        si=a1/sqrt(ef)
        x=x*(1.d0+si*ai2)
        y=y*(1.d0+si*ai2)
    endif
    endsubroutine

    subroutine tri_vol(r1,r2,r3,vol)
    implicit real*8(A-H,O-Z)
    dimension r1(3),r2(3),r3(3)
    vol=(r1(3)+r2(3)+r3(3))*0.166666666666666667d0
    vol=vol*(r1(1)*r2(2)-r2(1)*r1(2)+r2(1)*r3(2)-r3(1)*r2(2)+r3(1)*r1(2)-r1(1)*r3(2))
    vol=abs(vol)
    endsubroutine

    subroutine ttr_vol(r1,r2,r3,vol)
    implicit real*8(A-H,O-Z)
    dimension r1(3),r2(3),r3(3)
    vol=r1(1)*(r2(2)*r3(3)-r3(2)*r2(3))
    vol=vol+r2(1)*(r3(2)*r1(3)-r1(2)*r3(3))
    vol=vol+r3(1)*(r1(2)*r2(3)-r2(2)*r1(3))
    vol=abs(vol*0.166666666666666667d0)
    endsubroutine
