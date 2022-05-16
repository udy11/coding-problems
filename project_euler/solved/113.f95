! TRANSFER-MATRIX METHOD

    implicit integer*8(I-N)
    dimension mi(10,10),md(10,10),ni(10),nd(10)
    
    mi=0; ni=1; ni(1)=0
    md=0; nd=1; nd(1)=0
    do i=1,10
        do j=1,10
            if(i>=j) mi(i,j)=1
            if(i<=j) md(i,j)=1
        enddo
    enddo
    
    nnbs=9
    do k=1,100
        ni=matmul(mi,ni)
        nd=matmul(md,nd)
        nnb=sum(ni)+sum(nd)-9
        nnbs=nnbs+nnb
        write(6,*) k+1,nnbs
    enddo
    end
