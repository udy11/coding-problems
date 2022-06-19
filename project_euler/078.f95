! EULER's PENTAGONAL NUMBER THEOREM (with Sieve approach)

! Basically, generate partition numbers using that Euler's theorem
! using Sieve, while keeping numbers below 10^8
! Then later check if any is divisible by 10^6

    implicit integer*8(I-N)
    dimension ipns(0:1000000),ipt(4000)
    ipns=0
    ipns(0)=1
    do k=1,2000
        ipt(2*k-1)=k*(3*k-1)/2
        ipt(2*k)=-k*(-3*k-1)/2
    enddo
    nw=100000000
    nn=60000
    do i=0,nn
        j=1
        ns=1
        do while(ipt(j+1)<=nn)
            ipns(i+ipt(j))=ipns(i+ipt(j))+ns*ipns(i)
            ipns(i+ipt(j+1))=ipns(i+ipt(j+1))+ns*ipns(i)
            if(ipns(i+ipt(j))>nw) then
                ipns(i+ipt(j))=mod(ipns(i+ipt(j)),nw)
            endif
            if(ipns(i+ipt(j+1))>nw) then
                ipns(i+ipt(j+1))=mod(ipns(i+ipt(j+1)),nw)
            endif
            if(ipns(i+ipt(j))<=0) then
                ipns(i+ipt(j))=ipns(i+ipt(j))+nw
            endif
            if(ipns(i+ipt(j+1))<=0) then
                ipns(i+ipt(j+1))=ipns(i+ipt(j+1))+nw
            endif
            j=j+2
            ns=ns*(-1)
        enddo
    enddo
    do i=1,nn
        if(mod(ipns(i),1000000)==0) then
            write(6,*) i
            stop
        endif
    enddo
    end
