	do k=1998,200,-1
    	do j=999,100,-1
        	if((k-j)>999 .or. (k-j)<100) goto 1
			n=j*(k-j)
            n6=n/100000
            n1=mod(n,10)
            n5=mod(n,100000)/10000
            n2=mod(n,100)/10
            n4=mod(n,10000)/1000
            n3=mod(n,1000)/100
            if(n/100000/=0) then
            	if(n1==n6 .and. n2==n5 .and. n3==n4) then
                    goto 2
                end if
                else
                  if(n1==n5 .and. n2==n4) then
                    goto 2
                  end if
             end if
        end do
1		continue
	end do
2	print *,n,j,(k-j)
	end