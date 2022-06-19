n=100000000000; p=1;
for i=1:7830457
    p=p*2;
    p=mod(p,n);
end
p=p*28433+1;
format long
p