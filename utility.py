import json
import parse_story_format as parse_fn
import random
from collections import defaultdict
import os
import logging

logger = logging.getLogger(name='VIST_selfEval.database')

logger.setLevel(logging.DEBUG)


class Database():
    def __init__(self):
        self.story_id2images = {}
        self.team2story_id2story = {}
        self.now_running = []
        self.team2rank = defaultdict(int)
        self.rank_counter = 0

    def loads(self, setting, story_files):
        story_id2images_path = f'./data/{setting}_story_id2images.json'
        if not os.path.exists(story_id2images_path):
            raise ValueError(
                f'Please first generate {story_id2images_path} for this setting. More detail see the README')
        with open(story_id2images_path) as f:
            self.story_id2images = json.load(f)

        self.team2story_id2story = {}
        self.now_running = []
        self.team2rank = defaultdict(int)
        self.rank_counter = 0
        for story_file in story_files:
            file_path = os.path.join('./stories', setting, story_file)
            logger.debug(f'Loading story file: {file_path}')
            with open(file_path, 'r') as f:
                objs = json.load(f)
            if story_file.lower().startswith('glac') or story_file.lower().startswith('korea'):
                self.team2story_id2story[story_file] = parse_fn.parse_glac(
                    objs, self.story_id2images)
            elif story_file.lower().startswith('arel'):
                self.team2story_id2story[story_file] = parse_fn.parse_arel(
                    objs, self.story_id2images)
            elif story_file.lower().startswith('ground'):
                self.team2story_id2story[story_file] = parse_fn.parse_ground_truth(
                    objs, self.story_id2images)
            else:
                self.team2story_id2story[story_file] = parse_fn.parse_ours(
                    objs, self.story_id2images
                )
            self.now_running.append(f'{setting}/{story_file}')
        return True

    def update_score(self, rankings):
        rankings = rankings.split(',')
        for index, team in enumerate(rankings):
            self.team2rank[team] += index + 1
        self.rank_counter += 1
        logger.debug(f'team2rank: {self.team2rank}')
        logger.debug(f'self.rank_counter: {self.rank_counter}')

    def get_rank(self):
        return {k: round(v/self.rank_counter, 5) for k, v in self.team2rank.items()}

    def get_story_id2images(self):
        with open('../data/story_id2images.json', 'r') as f:
            return json.load(f)

    def get_random_stories(self):
        # get the story_id all team have generated story for
        story_ids = []
        for team, story_id2story in self.team2story_id2story.items():
            story_id = set(story_id2story.keys())
            story_ids.append(story_id)
        story_id_set = story_ids[0]
        for story_id in story_ids[1:]:
            story_id_set = story_id_set & story_id

        story_id = random.choice(list(story_id_set))
        story_list = []
        for team, story_id2story in self.team2story_id2story.items():
            story_list.append((team, story_id2story[story_id]))
        random.shuffle(story_list)
        return story_id, self.story_id2images[story_id], story_list
