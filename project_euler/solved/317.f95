! IDEA:
! Get the equation of all parabolas, i.e. y(x,theta)
! Maximize that w.r.t. theta, get equation for max y: y_max(x)
! Calculate the volume of rotation for this y_max(x) by rotating x

	implicit real*8(A-H,O-Z)
	integer*8 n
	a=0.0d0; b=120.3873598369011213d0; n=1000000
    pi=3.14159265358979324d0

	call int_smpsn_13(a,b,n,sm)
	write(6,*) sm
	end

	real*8 function fx(y)
	implicit real*8(A-H,O-Z)
    g=9.81d0
    pi=3.14159265358979324d0
    fx=pi*800.d0*(100.d0+200.d0/g-y)/g
	end function

! Simpson's 1/3rd Rule Subroutine
! Truncation Error = -(b-a)(h^4)f''''(z)/180, a<z<b
	subroutine int_smpsn_13(a,b,n,sm)
	implicit real*8(A-H,O-Z)
    integer*8 n
	h=(b-a)/(n*1.0d0)
	sm=h*(fx(a)+fx(b))/3.0d0
	do i=1,n/2
		sm=sm+h*(4.0d0*fx(a+(2*i-1)*h)+2.0d0*fx(a+2.0d0*i*h))/3.0d0
	end do
	if(mod(n,2)==0) sm=sm-2.0d0*h*fx(b)/3.0d0
	end
