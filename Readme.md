# Beautiful log

Pyhton filter script to make your access.log readble with [frontail]

## Requirements

```
npm i frontail -g
```

Do not forget to create filteredLog file

## lauching frontail

```
pm2 start 'frontail filteredLog' --name=Log
```

And visit http://127.0.0.1:9001

## If log file is in another machine
replace subprocess in app.py by your rsync command
and then run main.py everyday with crontab :
```
00 06 * * * root python3 /path/main.py
```

[frontail]: https://github.com/mthenw/frontail