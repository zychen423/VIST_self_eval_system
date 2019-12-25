# Intro
Sometimes I want to compare storis from several models before I send all of them to mTurks. But it is really easily to have bias if I simply open the result files and compare them. Therefore I wrote a simple web application that
1. load stories files
2. random choose a set of stories
3. and let user rank them and show the average ranks from multiple users

So in our team, once a model is trained, we put the generated story in the pool, set up several comparision, and ask all the team members to rank these stories. In the end we can have an idea if the model is getting better without really spend a lot of money in mTurk.

# Usage
### Prepration
make sure desired ```story_id2image``` is in ```data/```
put stories in the dir corresponding to the setting

1. prepare ```../data/{setting}_story_id2images.json``` for each setting. setting equal to the dir name in stories/
2. python3.6 server.py
3. go to [localhost:12588/setting.html](http://localhost:12588/setting.html) and set the story files you want to compare
4. go to [localhost:12588/scoring.html](http://localhost:12588/scoring.html) and start rank some stories!
5. go back to [localhost:12588/setting.html](http://localhost:12588/setting.html) and check result at the bottom of the webpage.

### API
```http://dorami.iis.sinica.edu.tw:12588/api?action=[action]&[key]=[value]```
