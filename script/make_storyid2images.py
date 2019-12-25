import json
from collections import defaultdict

''' Make the mapping: story_id -> [photo_flickr_id] 
for the original 5 image setting. Here the original 5 image setting
means "no randomly replaces" and is not the 3 image setting. This is
the story_id 2 images in VIST dataset. 
'''

story_id2images = defaultdict(list)
with open(f'../stories/3images/VIST_VG_hop_1.5_3paths_3terms.json', 'r') as f:
    objs = json.load(f)
    for obj in objs:
        story_id = obj['story_id']
        flickr_id = obj['photo_flickr_id']
        if flickr_id not in story_id2images[story_id]:
            story_id2images[story_id].append(flickr_id)
for story_id in story_id2images:
    story_id2images[story_id] = story_id2images[story_id][1:-1]
for story_id, images in story_id2images.items():
    assert len(images) == 3


with open('../data/3images_story_id2images.json', 'w') as f:
    json.dump(story_id2images, f)
