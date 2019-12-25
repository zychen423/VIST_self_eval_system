import tornado.web
import tornado.ioloop
import os
import json
from utility import Database
import logging

database = Database()
logger = logging.getLogger(name='VIST_selfEval')
logger.setLevel(logging.DEBUG)


class NoCacheStaticFileHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")


class WebHandler(tornado.web.RequestHandler):
    def initialize(self, database):
        self.database = database
        self.action2func = {
            'get_setting_list': self._get_setting_list,
            'get_story_list': self._get_story_list,
            'ranking': self._ranking,
            'get_rank': self._get_rank,
            'use_these_files': self._use_these_files,
            'get_now_running': self._get_now_running,
            'get_stories_to_rank': self._get_stories_to_rank,
        }

    def get(self):
        logger.info(f'Get request:{self.request.uri}')
        action = self.get_argument('action')
        self.action2func[action]()
        self.finish()
        return

    def _get_setting_list(self):
        settings = os.listdir('./stories')
        self.write(json.dumps(settings))

    def _get_story_list(self):
        setting = self.get_argument('setting')
        story_files = os.listdir(os.path.join('./stories', setting))
        self.write(json.dumps(story_files))

    def _ranking(self):
        rankings = self.get_argument('ranks')
        self.database.update_score(rankings)
        self.write(json.dumps({'status': True}))

    def _get_rank(self):
        ranks = self.database.get_rank()
        self.write(json.dumps(ranks))

    def _use_these_files(self):
        setting = self.get_argument('setting')
        story_files = self.get_argument('story_files').split(',')
        self.database.loads(setting=setting, story_files=story_files)
        self._get_now_running()

    def _get_now_running(self):
        self.write(json.dumps(self.database.now_running))

    def _get_stories_to_rank(self):
        # if not setting before:
        if len(self.database.team2story_id2story) == 0:
            raise ValueError('Please first set the story to use')
        story_id, images, story_list = self.database.get_random_stories()
        obj = {'story_id': story_id, 'images': images,
               'story_list': story_list}
        self.write(json.dumps(obj))


handlers = [(r'/api', WebHandler, dict(database=database)),
            (r'/(.*)', NoCacheStaticFileHandler, {"path": './static'})]

application = tornado.web.Application(handlers)
application.listen(12588)
logger.debug(f'Running at port 12588')
tornado.ioloop.IOLoop.instance().start()
