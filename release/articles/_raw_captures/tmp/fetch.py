import sys, re, html, subprocess, os
url=sys.argv[1]; out=sys.argv[2]
raw=out+'.html'
subprocess.run(['curl','-s','-x','http://127.0.0.1:7890','-L','--compressed','-A','Mozilla/5.0 (Windows NT 10.0; Win64; x64)','--max-time','90',url,'-o',raw],check=False)
try:
    s=open(raw,encoding='utf-8',errors='ignore').read()
except Exception as e:
    print('ERR',e); sys.exit(1)
s=re.sub(r'<script.*?</script>','',s,flags=re.S|re.I)
s=re.sub(r'<style.*?</style>','',s,flags=re.S|re.I)
s=re.sub(r'<br\s*/?>','\n',s,flags=re.I)
s=re.sub(r'</p>','\n',s,flags=re.I)
s=re.sub(r'<[^>]+>','\n',s)
s=html.unescape(s)
lines=[l.strip() for l in s.split('\n') if l.strip()]
txt='\n'.join(lines)
open(out+'.txt','w',encoding='utf-8').write(txt)
print('OK',len(txt),out+'.txt')
