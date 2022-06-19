s=0;
n=1000000000000;
for i=1:1000
    p=1;
    for j=1:i
        p=p*i;
        p=mod(p,n);
    end
    s=s+p;
end
format long
s