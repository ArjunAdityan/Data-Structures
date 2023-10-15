def compute_lps(pat,m,lps):
  len=0
  i=1
  lps[0]=0
  while i<m:
    if pat[i]==pat[len]:
      lps[i]=len+1
      len+=1
      i+=1
    else:
      if len!=0:
        len=lps[len-1]
      else:
        lps[i]=0
        i+=1
def kmp(pat,txt):
  m=len(pat)
  n=len(txt)
  lps=[0]*m
  compute_lps(pat,m,lps)
  i=0
  j=0
  while i<n and j<m:
    if pat[j]==txt[i]:
      i+=1
      j+=1
    else:
      if j!=0:
        j=lps[j-1]
      else:
        i+=1
    if j==m:
      print("The pattern is found at index",i-j)
      j=lps[j-1]

txt='AABAACAADAABAABA'
pat='AABA'
kmp(pat,txt)


'''n=int(input("enter the length of text:"))
txt=''
for i in range(n):
  element=input("enter the element of text:")
  txt+element
text=txt
m=int(input("enter the length of pattern:"))
pat=''
for i in range(m):
  element=input("enter the element of text:")
  pat+element
pattern=pat'''