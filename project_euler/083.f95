! DIJKSTRA'S ALGORITHM

! My 100th

    dimension m0(80,80),m1(80,80)
    dimension mc(6400,3),ii(2),jj(4,2)
    logical cc,dd(80,80)

! Initializations
    open(83,file='083_matrix.txt')
    n=80
    do i=1,n
        read(83,*) (m0(i,j),j=1,n)
    enddo
    mc=0
    mc(1,1)=1; mc(1,2)=1
    m1=99999999
    m1(1,1)=m0(1,1)
    ii(1)=1; ii(2)=1
    dd=.false.
    kc=0

    do while(mc(kc,1)/=n .or. mc(kc,2)/=n)
        kc=kc+1
        mc(kc,1)=ii(1); mc(kc,2)=ii(2)
        mc(kc,3)=m1(ii(1),ii(2))
        jj(1,1)=ii(1)-1; jj(1,2)=ii(2)
        jj(2,1)=ii(1); jj(2,2)=ii(2)-1
        jj(3,1)=ii(1)+1; jj(3,2)=ii(2)
        jj(4,1)=ii(1); jj(4,2)=ii(2)+1
        do j=1,4
            cc=.true.
            do k=1,kc
                if(jj(j,1)==mc(k,1) .and. jj(j,2)==mc(k,2)) then
                    cc=.false.
                    exit
                endif
            enddo
            if(jj(j,1)<1 .or. jj(j,2)<1) cc=.false.
            if(jj(j,1)>n .or. jj(j,2)>n) cc=.false.
            ms=m0(jj(j,1),jj(j,2))+mc(kc,3)
            if(cc .and. ms<m1(jj(j,1),jj(j,2))) then
                m1(jj(j,1),jj(j,2))=ms
                dd(jj(j,1),jj(j,2))=.true.
            endif
        enddo
        imn=99999999
        do i=1,n
            do j=1,n
              if(dd(i,j) .and. m1(i,j)<imn) then
                  ii(1)=i; ii(2)=j
                  imn=m1(i,j)
              endif
            enddo
        enddo
        dd(ii(1),ii(2))=.false.
    enddo

    write(6,*) m1(n,n)

    end
