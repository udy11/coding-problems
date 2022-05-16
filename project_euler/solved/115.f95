! TRANSFER MATRIX METHOD

    implicit integer*8(I-N)

    dimension ia(51,51),ib(51)

    ia=0; ib=0

    ia(1,1)=1; ia(1,2)=1

    do i=2,50
        ia(i,i+1)=1
    enddo

    ia(51,1)=1; ia(51,51)=1

    ib(1)=1; ib(51)=1

    j=0
    do while(sum(ib)<1000000)
        ib=matmul(ia,ib)
        j=j+1
    enddo

    write(6,*) j+50

    end
