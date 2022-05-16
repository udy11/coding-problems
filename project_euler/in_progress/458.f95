    implicit integer*16(I-N)
    n=int(1.d9,8)
    k=int(1.d12,8)
    m=282475249
    m0=282475249-2016840
    m1=m
    i=1
    do while(i<7)
        do j=1,9
            m0=mod(m0*m,k)
            m1=mod(m1*m,k)
        enddo
        m=m1
        i=i+1
    enddo
    write(6,*) m0+840
    end
