# Prepration
make sure desired ```story_id2image``` is in ```data/```
put stories in the dir corresponding to the setting

# API
```http://dorami.iis.sinica.edu.tw:12588/api?action=[action]&[key]=[value]```

## Usage
1. prepare ```../data/{setting}_story_id2images.json``` for each setting. setting equal to the dir name in stories/
2. python3.6 server.py
3. go to [localhost:12588/setting.html](localhost:12588/setting.html) and set the story files you want to compare
4. go to [localhost:12588/scoring.html](localhost:12588/scoring.html) and start rank some stories!
5. go back to [localhost:12588/setting.html](localhost:12588/setting.html) and check result at the bottom of the webpage.

