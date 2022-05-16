! TRANSFER MATRIX METHOD

    implicit integer*8(I-N)

    dimension m1(2,2),m2(2,2),m3(2,2),m4(2,2),n1(2),n2(2)

    m1(1,1)=30; m1(1,2)=25; m1(2,1)=0;  m1(2,2)=0
    m2(1,1)=30; m2(1,2)=25; m2(2,1)=20; m2(2,2)=25
    m3(1,1)=0;  m3(1,2)=0;  m3(2,1)=20; m3(2,2)=25
    m4(1,1)=0;  m4(1,2)=5;  m4(2,1)=0;  m4(2,2)=0

    n1(1)=20; n1(2)=0
    n2(1)=0;  n2(2)=20

! For 2 digits:
    k2 = sum(n1)

! For 3 digits:
    k3 = sum(matmul(m4,n2))

! For 4 digits:
    k4 = sum(matmul(m1,n1))

! For 5 digits:
    k5 = 0

! For 6 digits:
    k6 = sum(matmul(m1,matmul(m1,n1)))

! For 7 digits:
    k7 = sum(matmul(m4,matmul(m3,matmul(m1,n2))))

! For 8 digits:
    k8 = sum(matmul(m1,matmul(m1,matmul(m1,n1))))

! For 9 digits:
    k9 = 0

    write(6,*) k2+k3+k4+k5+k6+k7+k8+k9

    end
