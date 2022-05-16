	r=132.53:1.0E-05:132.54;
	theta=1.0:1.0E-04:pi/2.0;
	[R,THETA]=meshgrid(r,theta);
	A=2.0*(125000 - R.^2.0 + THETA.*R.^2.0 + cos(THETA).*R.^2.0 - sin(THETA).*R.^2.0);
	P=4.0*(500 + R.*THETA - 2.0*sqrt(2.0)*R.*sin(THETA./2.0));
	Z=A./P;
	xlabel('R');
	ylabel('THETA');
	contour(R,THETA,Z)
