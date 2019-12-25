''' Here define all the function for parsing different generated stories format.
Return a story_id2story dict.

'''


def parse_glac(objs, story_id2images):
    image2story_id = {'_'.join(v): k for k, v in story_id2images.items()}
    story_id2story = {}
    for obj in objs['output_stories']:
        images = obj['photo_sequence']
        story = obj['story_text_normalized']
        if '_'.join(images) in image2story_id:
            story_id = image2story_id['_'.join(images)]
        story_id2story[story_id] = story
    return story_id2story


def parse_arel(objs, story_id2images):
    ''' Not going to implement this until we discuss the arel format
    '''
    return False


def parse_ground_truth(objs, story_id2images):
    story_id2story = {}
    image2story_id = {'_'.join(v): k for k, v in story_id2images.items()}
    for album_image, story in objs.items():
        images = album_image.split('/')[1:]
        if '_'.join(images) in image2story_id:
            story_id = image2story_id['_'.join(images)]
        story_id2story[story_id] = story
    return story_id2story


def parse_ours(objs, story_id2images):
    story_id2story = {}
    for obj in objs:
        story_id = obj['story_id']
        if 'predicted_story' in obj:
            story = obj['predicted_story']
        elif 'add_one_path_story' in obj:
            story = obj['add_one_path_story']
        story_id2story[story_id] = story
    return story_id2story
