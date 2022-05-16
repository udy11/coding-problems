! TRANSFER MATRIX METHOD

    implicit integer*8(I-N)

    dimension ia(4,4),ib(4)

    ia(1,:)=(/ 1,1,0,0 /)
    ia(2,:)=(/ 0,0,1,0 /)
    ia(3,:)=(/ 0,0,0,1 /)
    ia(4,:)=(/ 1,0,0,1 /)

    ib=(/ 1,0,0,1 /)

    do j=1,47
        ib=matmul(ia,ib)
    enddo

    write(6,*) sum(ib)

    end
