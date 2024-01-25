from time import sleep
import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_username(self):
        username = str(self.username)
        username_len = len(username) >= 6 and len(username) <= 30
        if ".." in username:
            return False
        return username_len and (username.isalpha() or username.isdigit() or "." in username)

    def check_password(self):
        password = str(self.password)
        password_len = len(password) >= 8 and len(password) <= 128
        return password_len and not password.isspace()
    
    def check(self):
        print("Chesking...")
        sleep(3)
        if self.check_password() and self.check_username():
            print("Successful: Your password and username are safe and secure")
        else:
            print("Failed: Your password or username does not meet the requirements\n\n")
            random_pass = input("Shall I generate a new password for you? Yes=1/No=0: ")
            if random_pass == "1":
                print("Generating new password...")
                sleep(2)
                print(f"Your new password:  {self.random_password()}")
            else:
                print("OK.")
    
    #Qo'shimcha      
    def random_password(self):
        passwords = ['v9dBiSet[+]', '7f13eu.R!/p]PD', '*e}-\\6wY6{Mo+N\\4+@', '7\'x1bm\\31\\$D^7?^6""!', '^e$zTz9n!#rN4XHM~<N', '*4Wo1IQ%j|S7a9H', 'G"j[f1W6cs\'k<6zY', 'hvhJPm3<JJ-4|BLG>S!', "3HHIxTS14Nv<Gv8';'dl", 'Ki.5,#025Z3f&A:JG_:', 'S[l&dIo|9226joym', '}U=^s&Yt12>9q', "nH\\i:'Tfa3E,aMO9p;2", 'so7mV?%L:!1', '6q!3,Ae?PyN[6', '@6oLysi+juC\\-<k3?_do', 'eTmSTh(3qt/AC<i5', '8qAuP9)E24maAE;vM', 'i.[T:sQZ6iw', "clVYx3@DCT0&yur6i'P", '8K1bq0HT_', '=@l9S0oW', 's"!OHu@8{{xUi', '#QuNX!1T}2pa', 'KDBtjsA$)LX*?Y@!4', '}KfY3lp+0>ZR', 'cJ|@R|Rn%d*Bx7"oJ?B', '7zI}5xRU@lj', 'b^?Nr17],wfW//5y{D', 'A@siu9SU', '36fR$q)upx', "@=S1W'G/}CQ`pwV[<", '%?d6zIfgzh_{r', 'Z8\\QsjsAL5', '.71q\\)@X*jE<&Ka$lI]l', "(h1Qw$',ZJBO9.Va,sXM", '.0>,6a3~HV]i~(HXS', 'kj`]M_8Ol#zy', '<T)s*FWhZQH!fJ&#U0\\', 'L9Nb(B8xg[k0`;b', '0e:]%)hBRC/=Y', 'dCLR.[zd*\\2{2cbN', 'LBssbfOG6?*]', 'qVw>M}4)VaB9j)la^e', '12:s@fs+X]d<mei', '+Wce};xkJ;w8yvQ!\\M9', "C'c2E?$?|EgHiK3~h9E", '-z=w\\9W-|AN#%', 'VJ3nj36Gy<RR1KNT,=r', '(s9PiBPic', '?O{F29[Mf4', 'MM,4c<g:$)/a[3}nOBF1', 'E_*$3s[7+V', "r5@HtXq{ZZEVh2'u_", 'AUcedDW8SgsQ#Cx<TI$i', '90!_:>o4I&9mcx^U`o', '3R$]6OIak', 'C4jR(0d{V=sJkB2m:', '?pi":\\$`PH:h)q6rL', '8^!0F7-g-,Mj@8J', 'Ks9J^(gd4)+', 'Kex2H*,Ax0dy\'^"5', '/D<}}Y2j]asc', 'c>CgJ1M[q7GdOewW7a', '6aJ5X.GX', '(_b7ooYozxX4', '<o${C-|96V:I', 'D\\S(Hvcx7_<]Qiwz@Qi2', 'F/@I?QiNt2', 'qv7y+n{9\\mcH)uKE2', "8r7Axh'PXEs", "'+RCdMV-t?%3>mj", 'nvuv=!*Y<gTO*9n', '\\`+wP6SNU', 'A%c0J94+C!,fZN*!', 'GY%s*?H(Y.,9bd9', '/o~lM9B:', '9"Sf/}4:nqQ', 'w;%0yQ)Rq;+(>', ',}oUNpj99~`N|t{"Sw2', '31zYbDW<pL7q', '1|2EA`vlWOv', ']5{D|uD;>(', 'a`t<CZ-qw:kN4%3v', 'LV4K^W2pc).jc', '+IGMh-wKZ,_:2[2#vLrj', '<I<@ln)c7U', 'C?lqEY3{I', "r2p9E!'+6M&YB", '(WRn#"6~[+/l', '!mvI6lG+ip', 'f{!.N!Bc9b*A#w];Tt~`', 'g^,8{(Xp6.%C|d', 'SLY1@h.5.VQdp~p', '5]lHn30<I+', 'O50SxR@|XwB.', 'xFuqKXI\\wEgZ7[-', "b8Xk~$'6", ':`dM2Yl^{H5Q', '~ED+5jjp-qAq']
        return random.choice(passwords)


p = User("salogjkgj...jjm", "A%c0J94+C!,fZN*!")
p.check()
