! TRANSFER MATRIX METHOD

    implicit integer*16(I-N)

    dimension ia(4,4),ib(4)

    ia(1,:)=(/1,1,0,0/)
    ia(2,:)=(/0,0,1,0/)
    ia(3,:)=(/0,0,0,1/)
    ia(4,:)=(/3,2,1,0/)

    ib=(/1,0,1,2/)

    do j=4,50
        ib=matmul(ia,ib)
    enddo

    write(6,*) sum(ib)

    end
