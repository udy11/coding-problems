    integer sdk(9,9),sdkp(9,9,9),ijnp(9,2),ijyp(9,2),ijf(6)
    open(1,file='096_tr.txt')
    ts=0; nml=362880

! Pre-allocating possibility array sdkp
    do i=1,9
    do j=1,9
        do k=1,9
            sdkp(i,j,k)=k
        enddo
    enddo
    enddo

! Reading Sudoku, setting appropriate sdkp entries
    do i=1,9
        read(1,*) k
        m=k
        do j=1,9
            sdk(i,j)=m/(10**(9-j))
            if(sdk(i,j)/=0) then
                call sdkp_st(sdkp,sdk(i,j),i,j)
                ts=ts+1
                print *,'Filled:',i,j,5
            endif
            m=m-(m/(10**(9-j)))*10**(9-j)
        enddo
    enddo
    close(1)

!    while(ts<81) do
    do nn=1,10
    do i=1,9
    do j=1,9

! For a zero entry in sdk, checking if only one entry is possible
! If yes, filling it and setting appropriate entries in sdkp
    if(sdk(i,j)==0) then
        do k=1,9
            if(sdk(i,k)/=0) then
                sdkp(i,j,sdk(i,k))=sdkp(i,j,sdk(i,k))*0
            endif
            if(sdk(k,j)/=0) then
                sdkp(i,j,sdk(k,j))=sdkp(i,j,sdk(k,j))*0
            endif
            ii=1+3*((i-1)/3)+(k-1)/3; jj=1+3*((j-1)/3)+mod(k-1,3)
            if(sdk(ii,jj)/=0) then
                sdkp(i,j,sdk(ii,jj))=sdkp(i,j,sdk(ii,jj))*0
            endif
        enddo

        ijs=0; ijc=1
        do k=1,9
            if(sdkp(i,j,k)==0) then
                ijs=ijs+1
                ijc=ijc*k
            endif
        enddo
        if(ijs==8) then
            sdk(i,j)=nml/ijc
            call sdkp_st(sdkp,sdk(i,j),i,j)
            ts=ts+1
            print *,'Filled:',i,j,1
        endif
    endif

! For a zero entry in sdk, checking BOX-wise if there is a
! number which cannot come anywhere else
    if(sdk(i,j)==0) then
        call fl_nmb(sdk,i,j,ijnp,ijyp,kn,ky,1,1)
        ijbfc=0; k=1
        while(k<10 .and. ijbfc==0) do
        ijns=0; ijys=0
        do l=1,ky
            ijys=ijys+sdkp(ijyp(l,1),ijyp(l,2),k)
        enddo
        if(ijys==0) then
            do l=1,kn
                if(sdk(ijnp(l,1),ijnp(l,2))==k) ijys=ijys+k
            enddo
            if(ijys==0) then
                sdk(i,j)=k
                call sdkp_st(sdkp,sdk(i,j),i,j)
                ts=ts+1
                print *,'Filled:',i,j,2
                ijbfc=1
            endif
        endif
        k=k+1
        endwhile
    endif

! For a zero entry in sdk, checking ROW-wise if there is a
! number which cannot come anywhere else
    if(sdk(i,j)==0) then
        call fl_nmb(sdk,i,j,ijnp,ijyp,kn,ky,3,1)
        ijrfc=0
        while(k<10 .and. ijrfc==0) do
        ijns=0; ijys=0
        do l=1,ky
            ijys=ijys+sdkp(ijyp(l,1),ijyp(l,2),k)
        enddo
        if(ijys==0) then
            do l=1,kn
                if(sdk(ijnp(l,1),ijnp(l,2))==k) ijys=ijys+k
            enddo
            if(ijys==0) then
                sdk(i,j)=k
                call sdkp_st(sdkp,sdk(i,j),i,j)
                ts=ts+1
                print *,'Filled:',i,j,3
                ijrfc=1
            endif
        endif
        k=k+1
        endwhile
    endif

! For a zero entry in sdk, checking COLUMN-wise if there is a
! number which cannot come anywhere else
    if(sdk(i,j)==0) then
        call fl_nmb(sdk,i,j,ijnp,ijyp,kn,ky,2,1)
        ijcfc=0
        while(k<10 .and. ijcfc==0) do
        ijns=0; ijys=0
        do l=1,ky
            ijys=ijys+sdkp(ijyp(l,1),ijyp(l,2),k)
        enddo
        if(ijys==0) then
            do l=1,kn
                if(sdk(ijnp(l,1),ijnp(l,2))==k) ijys=ijys+k
            enddo
            if(ijys==0) then
                sdk(i,j)=k
                call sdkp_st(sdkp,sdk(i,j),i,j)
                ts=ts+1
                print *,'Filled:',i,j,4
                ijcfc=1
            endif
        endif
        endwhile
    endif

    enddo
    enddo

! Row-Column Refinement of sdkp based on Box
    do i=1,9
    do j=1,7,3
        call nr_nmb(i,i1,i2)
        do k=1,9
        is2=0; js2=0
        do ks=0,2
            is2=is2+sdkp(i1,j+ks,k)
            is2=is2+sdkp(i2,j+ks,k)
            js2=js2+sdkp(j+ks,i1,k)
            js2=js2+sdkp(j+ks,i2,k)
        enddo
        if(is2==0) then
            is1=0
            do ks=0,2
                is1=is1+sdkp(i,j+ks,k)
            enddo
            if(is1>=2*k) then
                call fr_nmb(j,ijf)
                do kk=1,6
                    sdkp(i,ijf(kk),k)=0
                enddo
            endif
        endif
        if(js2==0) then
            js1=0
            do ks=0,2
                js1=js1+sdkp(j+ks,i,k)
            enddo
            if(js1>=2*k) then
                call fr_nmb(j,ijf)
                do kk=1,6
                    sdkp(ijf(kk),i,k)=0
                enddo
            endif
        endif
        enddo
    enddo
    enddo

! Box Refinement of sdkp based on Row-Column
    do i=1,9
    do j=1,7,3
        call fr_nmb(j,ijf)
        do k=1,9
        is2=0; js2=0
        do ks=1,6
            is2=is2+sdkp(i,ijf(ks),k)
            js2=js2+sdkp(ijf(ks),i,k)
        enddo
        if(is2==0) then
            is1=0
            do ks=0,2
                is1=is1+sdkp(i,j+ks,k)
            enddo
            if(is1>=2*k) then
                call nr_nmb(i,i1,i2)
                do kk=0,2
                    sdkp(i1,j+kk,k)=0
                    sdkp(i2,j+kk,k)=0
                enddo
            endif
        endif
        if(js2==0) then
            js1=0
            do ks=0,2
                js1=js1+sdkp(j+ks,i,k)
            enddo
            if(js1>=2*k) then
                call nr_nmb(i,i1,i2)
                do kk=0,2
                    sdkp(j+kk,i1,k)=0
                    sdkp(j+kk,i2,k)=0
                enddo
            endif
        endif
        enddo
    enddo
    enddo

    print *,ts
    enddo
!    endwhile

    call sdk_chk(sdk,ni)
    print *,ni

! Writing final data
    open(2,file='96_tr_ps.txt')
    do i=1,9
    do j=1,9
        write(2,'(11I3)') i,j,sdkp(i,j,:)
    enddo
    enddo

    open(3,file='96_tr_out.txt')
    do i=1,9
        write(3,'(11I3)') sdk(i,:)
    enddo

    end

! Subroutine to get near 2 numbers like
! 2->1,3; 1->2,3; 7->8,9; etc...
    subroutine nr_nmb(i,j,k)
    integer,intent(in) :: i
    integer,intent(out) :: j,k
    m=3*((i-1)/3)
    j=mod(mod(i,3)+1,3)
    if(j==0) j=3
    k=mod(mod(i,3)+2,3)
    if(k==0) k=3
    j=j+m
    k=k+m
    endsubroutine

! Subroutine to get far 6 numbers like
! 1->4,5,6,7,8,9; 5->1,2,3,7,8,9
    subroutine fr_nmb(i,j)
    integer,intent(in) :: i
    integer,intent(out) :: j(6)
    m=1+(i-1)/3
    call nr_nmb(m,m1,m2)
    do k=1,3
        j(k)=(m1-1)*3+k
        j(k+3)=(m2-1)*3+k
    enddo
    endsubroutine

! Subroutine to set sdkp depending on sdk's new entry
    subroutine sdkp_st(sdkp,vl,i,j)
    integer,intent(in) :: vl,i,j
    integer,intent(inout) :: sdkp(9,9,9)
    sdkp(i,j,:)=0
    sdkp(:,j,vl)=0
    sdkp(i,:,vl)=0
    do k=1,9
        ii=1+3*((i-1)/3)+(k-1)/3; jj=1+3*((j-1)/3)+mod(k-1,3)
        sdkp(ii,jj,vl)=0
    enddo
    endsubroutine

! Subroutine to get filled and non-filled entries in ij-box,
! j-column, i-row decided by bcr=1,2,3 respectively
! Whether i-j itself be included or not can be decided by nij=2,1
    subroutine fl_nmb(sdk,i,j,ijnp,ijyp,kn,ky,bcr,nij)
    integer,intent(in) :: i,j,sdk(9,9),bcr,nij
    integer,intent(out) :: ijnp(9,2),ijyp(9,2),kn,ky
    ijnp=0; ijyp=0; kn=0; ky=0
    do k=1,9
        if(bcr==1) then
            ii=1+3*((i-1)/3)+(k-1)/3
            jj=1+3*((j-1)/3)+mod(k-1,3)
        endif
        if(bcr==2) then
            ii=k
            jj=j
        endif
        if(bcr==3) then
            ii=i
            jj=k
        endif
        if(sdk(ii,jj)/=0) then
            kn=kn+1
            ijnp(kn,1)=ii; ijnp(kn,2)=jj
        elseif(nij==1 .and. ii*10+jj/=i*10+j) then
            ky=ky+1
            ijyp(ky,1)=ii; ijyp(ky,2)=jj
        elseif(nij==2) then
            ky=ky+1
            ijyp(ky,1)=ii; ijyp(ky,2)=jj
        endif
    enddo
    endsubroutine

! Subroutine to check the trivial consistency of Sudoku
! v=1 if consistent, 0 if not
    subroutine sdk_chk(sdk,v)
    integer,intent(in) :: sdk(9,9)
    integer,intent(out) :: v
    v=1
    do k=1,9
    do i=1,8
    do j=i+1,9
        if((sdk(k,i)==sdk(k,j) .and. sdk(k,i)/=0) .or. (sdk(i,k)==sdk(j,k) .and. sdk(i,k)/=0)) then
            v=0; goto 89
        endif
    enddo
    enddo
    enddo
    if(v==1) then
    do i=1,7,3
    do j=1,7,3
    do k1=0,7
    do k2=k1+1,8
        i1=i+k1/3; j1=j+mod(k1,3)
        i2=i+k2/3; j2=j+mod(k2,3)
        if(sdk(i1,j1)==sdk(i2,j2) .and. sdk(i1,j1)/=0) then
            v=0; goto 89
        endif
    enddo
    enddo
    enddo
    enddo
    endif
89  i=7
    endsubroutine
