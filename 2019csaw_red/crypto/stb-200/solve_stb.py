import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

e = 65537
n = long('144002415646646478674064490699377786192533270079924611620840630090057970493761515497557516515860491126117516461676923836446960846672404699605921347691384226831131977895716285832561574379078845884985040607117861236634693480538912293924994652655057830079960145315805141789726315489391843763675200548314830559313')
d = long('41322938643188687324470052708208314937056577868350736354232560382511790623478736304756327484558803826286358443879443186751602440803585440028361991323344324735400871499851005306829152634791235385604026297340654602738827790488253224821187558324555211141010441265230280642709773165613835085748369635458118817003')
p = long('11532905659490638432015415692520298221363196322702044447415743317014587627601924021065768367370028854667251963869589930603173492479382573175533930395611471')
q = long('12486221590492614857789513830375181167234875625546111646309674799383281534786643455228344889759625805646133423762164368046139054448526759595492728691831903')

key_args = (n, e, d, p, q)
key_rsa = RSA.construct(key_args)
key = PKCS1_OAEP.new(key_rsa)

m = "958d7a7a4490abe99fbdea2830c6002345421576c4a7413e874253bd5e4b6b30badf9ee52fe5c279b175025c6f0cbfbbcfa319501c585218a5a99458f2188e1df3e6c662a8b0e64152494a43e3d7ebafb5e0420bca37b6894ab5938d3e7e29f6aea39a561f584219b19622695464fa72b65a6f5a517008c86a7fd73e2774dd00".decode('hex')

print(key.decrypt(m))