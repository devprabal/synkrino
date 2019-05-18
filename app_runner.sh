cd syn/synkrino-master
source synenv/bin/activate
python3 app.py &
/usr/bin/firefox --new-tab http://0.0.0.0:3000 </dev/null &>/dev/null &
