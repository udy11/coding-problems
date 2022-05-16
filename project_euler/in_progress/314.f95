!pro

	PROGRAM sqmax

	REAL*8 ::r, angle, max, P, A, T, pi=3.14159265358979d0
	INTEGER*8 :: i

	OPEN(1, FILE='pro.dat')
	MAX=0

	DO i=241257,243257,1
	r=294.06+i*1.0E-08
	angle=(pi/4.0-acos(250.0/r))
	P=r*angle+sqrt(r*r-250.0*250.0)
	A=125.0*sqrt(r*r-250.0*250.0)+r*r*0.5*angle
	T=A/P
	IF(T>131.0)THEN
	WRITE(1, *) r, T
	END IF
	IF(t>MAX) MAX=t
	END DO

	CLOSE(1)
	print *,MAX

	END PROGRAM sqmax