! TRANSFER MATRIX METHOD

    implicit integer*8(I-N)

    dimension ia(5,5),ib(5)

    ns=0
    do k=2,4
        ia=0; ib=0
        ia(1,k)=1; ia(1,k+1)=1
        do i=2,k
            ia(i,i-1)=1
        enddo
        ia(k+1,k)=1; ia(k+1,k+1)=1
        ib(1)=1; ib(k+1)=1
        do j=k+1,50
            ib=matmul(ia,ib)
        enddo
        ns=ns+sum(ib)-1     ! minus one, because blank is not allowed
    enddo

    write(6,*) ns

    end
