jawab = 'ya'
while(jawab == 'ya'):
    no = input("NO :")
    nama = raw_input("NAMA :")
    nim = input("NIM :")
    nt= input("NILAI TUGAS :")
    nuts = input("NILAI UTS :")
    nuas = input("NILAI UAS :")
    nakhir = int(nt*30/100)+(nuts*35/100)+(nuas*35/100)
    nakhir = int(nt*30/100)+(nuts*35/100)+(nuas*35/100)
    jawab = raw_input("Tambah data (ya/tidak) :")
    if jawab == 'tidak':
        while(jawab == 'tidak'):
            print "____________________________________________________________"
            print "| NO | NAMA|  NIM  | N.TUGAS | N.UTS | N.UAS | N.AKHIR |"
            print "------------------------------------------------------------"
            print "|",no," | ",nama,"| ",nim,"|",nt,"|",nuts," |",nuas," |",nakhir,"|"
              


    
