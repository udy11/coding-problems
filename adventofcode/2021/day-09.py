import sys

in0 = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

in1 = '''9897656789865467895698765469899988672134598894345689864101378965457932349943210987654789653198789434
8789542499996878954329984398789976561012987789245678953212567892345791998899329899765678969997668912
7678943978987989965998993297649875432129876567956789864487678991056899877778939769886789998766457899
4578999868998996899867894976532986543299876476897899987569899989167898766567898654998898998655345678
2456987657679535679756799988643498657987654345789978899789998878998919954349997543219967987543237889
1234896545568986798645678999754989767898765456998769759899987765789329863238898659301256798793156891
2346789432379997987434689489899879898919876567899954346998796434678997642127789798512345989989247892
8756894210998989876545694378987868999101998688999863238987684323457789751015678987654459878678956994
9769995679876978998656789469876957893212999899989764649876576212345678953223489698866598754567897989
9878989989885467899787896598765648789329876959879986768985432101567789998654599549977987543468998978
3989879897654345689998998679954324595498754347669897979699564323459998949765678923989295432389989567
2997669789731287899899649799878212989987543233456789897598765434569767959878789313993197643578965456
9876548678954345997678998998965359878995432102345898795439896556978956899989895429894298754567989967
9754334567895456789567987897895498769896654233457987689649987667989349989999976598789349865678999898
8843212689986687993479876756789987656789999354569698789798998798996498679889988987679459996989239799
7654303568987798932349965345690976543245878965689459899987899899459987598679299998598998989993198677
9965214589298999421298764234892987632124567899893234999896757996598796476599101976467987979954989556
9876423499349988942359982123899876543012568998990123598765346989987654323478919765359896868899876434
9987834568959876899494321015789987654423458987781349987544235677898773212467899854298795756799764323
8798945679998975697985432123456799797634567896532398765432136456987654543588978975697654345878954212
6569987989897854586976543434589899898765778999994569976543012345699896698678967896989543234667994334
4323599999765632324989876565678935999876889998789678998652134456789998789789656799976532123456789765
3212678998654321012497987676799323497989996897678989998543445967997659899895346898798943434678999876
5323799998776432423456798989893214986797965986599999897654597888976545998921234987659975665789875987
5435678989886543434567899699954399865456797998989999798975679999987631987654345799543986796789653498
6547899767987656756778985467895987654357789219878797549986998921299890198765489898752397898997621359
7656999348999987897899876579999898983234679109767689920199887990123989989987568999643498959876533578
9767898769987899998986988989987689876123793298656577891298796789939878976597679998759979347987897689
0978999898776878999765399999976467965234999987545456792987665667898769897498989899898765456899989797
1999686999654767897654239899897379894349898765432345789876543456789456789329595789999876567988778965
9765534498743456899761098756789298789498789877521234568997431367890239899939424699998997879876567893
7654321239654569989943199645678999688997678988432345789789545689965498999898935988977898989865438942
8969210149875698779899986432349997567789499996544656795678957897896987898767899976756779995987546891
9898991268989987667678964321259986455679989987655767893567898956989876987656998765634567894398656789
8796989357899986554567893210198998234598776498789878912379939347978945698768987654323979976498787891
7645678968999975423589999321297986123987654339891989701588921299866734569979498962109898997569898910
8958789989998764312399998432986544016799543210910196532347893987654321368989329879298787898978929921
9769896599987655503457897553497432135698765432399987648656789499965873456993210998987656789989939892
7978965439876543217568998664987643446999876543478999759867892349876754567894329987542545691299899789
6989753212987654328678959989999987556899997664567899867999943458987876989965998765431236789498788678
5699975423498765449789543498965398698998998789678934979878956567998989990299879976742347999998679456
4579896534569896559895432346794298789877899898789013598867897678999998989987667988755458949876542367
3456798695678998678976544756891019899965789929992129987756789789787987867896545699766569439998956459
2348989989789989989987656897893434998754599545943298985645689897656986745899656899898678998989998567
1459879878999876592198987898964565989853678987894987674434568999749875434668968965929789987878987678
2598764267899986432019899999995679876542357998976986543223478998767976323456899654319898875468998989
4599879456789997543198778999989798764321345899989987664101249019879765414597968943101997654345989991
5988998968899898994987656789878999986430156789998698876832389323989986205689547894312987643234678990
9876987899976789789998767898765798765321269899876569997844678999999854319893236789323498753012399989
9754996899764244678959878999874859896442345789754323459998799878998765623989125899976569872123459878
9899875798943123579543999986543236987554567997654314368999892367899876754578934999898698943934569965
2987654987892013468932123499432125697665678999542101267987921257943988896679765698789987899895798754
3986543456794254778921019998954014598779799798653212346795210146792999987989879987679996989789987653
9875432345895345679543198787943123459989895698764423557984321235699765498999989876498785667679876542
2976983466795457799765987656964236598992924579876534989875432545989876329568996985349653446578987321
0989876567896768899876899767895347987891013468987975678987643459879998213467895695498742323459765435
1996997678998879989989999898976459876789123569098987789699776598765432109598996986569871015568977656
9875789789459989778999987999987598785468997679129898994566987679886545298989987897698762123459988767
8754679890345697669999875798998698654345689789234789543455799789998667987879998959797654255678999878
7543467991246789556987654567899899773298789896545678962434699898989879896567899539898765345689999989
8932345789757894345699765698932999974349899987858789910123988937678999765457895410999876789789898899
6521234599767892123469896989321298765999969998769897891239876723478998964346896321299987899895687799
7434345678978943014598989878935679976789458919878956792349765212567996654235789434989298965934545678
6545456989989432123987678967956789297992346901989545989998754201789875743124589665679129654321234569
7757567899997544539998789656897895498976469899895439877839765329899754321012678998798998765432345678
8767779987987656678929893245789999989899598765789921965321965445698765532343489999987769887674689799
9988989996598879789537942126897678976788987644686899975432987566789989763456789899876653998765678999
3299398965439998996545693437956569865567898632345678976545699978993599854667896798765432109876799989
2101267897546987898756989548943497654456789543956789597656901989432398765678945989997543212989899879
4212356998969996789899878959542349873247899859897894498969893496741349876789239876987655344599999868
5434567899198865567989759894321998989356798769799942349898789595432345987892123985498965455678998659
9656678999097654459878547789499876599967899998678921298797679987549976798999012494309876567789999543
8997889898998543267965436689987985439878999876567890987654598998998798999998923989212987679899898932
7789998757987653129754324578965699210989998765457991299843467899897689895987899878964598789999787893
5679987649876543019895412399954598462398999874346789987652359998786576794986799767895789894299696794
4599876434987432123976543467893497654457890975487995699764467986531345689765987656999899999987575989
5789864329876554994987674578932398765689932976699954349865879598765456899854399769899989998765464578
6899985410997689789098789689321539878789993987789893239878989459976567998743210998799979889954323567
7999878324989798679299898795430123989896789998995789145989991345987678999654321297698665767895434579
8998765439878986598987959896542234599945689879434679245996892399898889498766532976569543556789875699
9999897699765434497896545987665465689767898965323478959854953987679994349877659876398932346895986988
9987998987654323356799536599879878899899987899212367998743899876567895457999878985497893767994299877
9876599998763201245678923478989989954999976778923456987632788975479986679987989799986989899989198766
5987988998775412367889214567896597899889895567894599876543567987569997899976495698775778999878997654
4699867997654323989995323779943456999778794345965989987654578998678989929894334597664667898769876543
3798755798976437899976534589432239876665689459899878698786689989989678919789219987543558789656989632
2979843459987656789997849789540198765534569598798766539899789976594569998677998765432345678932398721
9867552345998768898989998997421999854323878997659854321998998895423998976566789879643458789210987210
8954431236899879967678987996539899965534989654339767320987896796579887895465678988756669895329976521
7643210348965989654589456789659799876645678962123988649875435989998756789324789999898779976498765434
8754325459954399767894345678998678997786899894235698798994323577899645678939899998969889876599886745
9765486567893239898976212799876567899897956789986789987432101456797434578998987897653999987689999656
9877578678975699999697434987656456999989345699998992196544312345976547689977476789542458998792498767
4988989789989789996598645998642345998765456789879019987665443767897658798765324567943567899891239978
3499599899998998989999799876321245789876567899865198798986556898998767987643213479957679935942997989
2323456989877987579899989765433357894998679989764398659397698949899979998765424567898997645699876598
1012369973256996456789964987655478943249789678965499543229899538789998769986535899999698759989765467
2123498764139865323898753599877699761029896567896987642109954324567898754398876789996549898768954356
4234599753019973210987654568989789732234989478998998764398765313456998673219998899875435999857895967
5346987542198765423499868679999897654345678989219239875987654324769876543101239912954323498767976879'''

def nbrs(i, j, nr, nc):
    nb = []
    if 0 < j < nc-1:
        nb.append((i, j-1))
        nb.append((i, j+1))
    elif j == 0:
        nb.append((i, 1))
    elif j == nc-1:
        nb.append((i, nc-2))
    if 0 < i < nr-1:
        nb.append((i-1, j))
        nb.append((i+1, j))
    elif i == 0:
        nb.append((1, j))
    elif i == nr-1:
        nb.append((nr-2, j))
    return nb

def basin(i, j, nr, nc, hs, bsn):
    nbs = nbrs(i, j, nr, nc)
    for nb in nbs:
        if not nb in bsn and hs[nb[0]][nb[1]] != 9:
            bsn.append(nb)
            basin(nb[0], nb[1], nr, nc, hs, bsn)

def p1(inp):
    hs = []
    for gs in inp.split('\n'):
        hs.append([int(g) for g in gs])
    nr = len(hs)
    nc = len(hs[0])

    rs = 0
    for i in range(nr):
        for j in range(nc):
            if all([hs[i][j] < hs[nb[0]][nb[1]] for nb in nbrs(i, j, nr, nc)]):
                rs += 1 + hs[i][j]
    return rs

def p2(inp):
    hs = []
    for gs in inp.split('\n'):
        hs.append([int(g) for g in gs])
    nr = len(hs)
    nc = len(hs[0])

    bsnl = []
    for i in range(nr):
        for j in range(nc):
            if all([hs[i][j] < hs[nb[0]][nb[1]] for nb in nbrs(i, j, nr, nc)]):
                bsnl.append((i, j))
    bsns = []
    for bl in bsnl:
        bsn = [bl]
        basin(bl[0], bl[1], nr, nc, hs, bsn)
        bsns.append(len(bsn))
    bsns.sort()
    return bsns[-1] * bsns[-2] * bsns[-3]

print('Soltion of Test Puzzle 1:', p1(in0))
print('Soltion of Puzzle 1:', p1(in1))
print('Soltion of Test Puzzle 2:', p2(in0))
print('Soltion of Puzzle 2:', p2(in1))
