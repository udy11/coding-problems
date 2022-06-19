! BRUTE-FORCE

! Checking if side lengths follow a*a+b*b=c*c

    integer a,b,c
    n=50
    m=0

    do i1=0,n
      do j1=0,n
        do i2=0,n
          do j2=0,n
            a=i1*i1+j1*j1
            b=i2*i2+j2*j2
            c=(i1-i2)**2+(j1-j2)**2
            if((a==b+c .or. b==a+c .or. c==a+b) .and. a>0 .and. b>0 .and. c>0) then
              m=m+1
              !write(6,*) i1,j1,i2,j2
            endif
          enddo
        enddo
      enddo
    enddo

    write(6,*) 'Total: ',m/2

    end
