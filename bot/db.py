import pymongo

class DB:
    def __init__(self, connection_string):
        self.c_string = connection_string
        self.__connect()

    def __connect(self):
        self.client = pymongo.MongoClient(self.c_string)
        self.db = self.client['hacktime']
        self.chats = self.db['chats']

    def __check_connection(self):
        try:
            self.chats.find({})
        except Exception:
            self.__connect()

    def check_chat(self, chat_id):
        self.__check_connection()
        try:
            ch = self.chats.find({'chat_id': chat_id})[0]
            return ch['_id']
        except:
            return False

    def add_chat(self, chat_id):
        self.__check_connection()
        if self.check_chat(chat_id):
            return False
        else:
            self.chats.insert_one({'chat_id': chat_id})
            return True

    def del_chat(self, chat_id):
        self.__check_connection()
        if not self.check_chat(chat_id):
            return False
        else:
            self.chats.delete_one({'chat_id': chat_id})
            return True

    def get_chats(self):
        chats = []
        self.__check_connection()
        ch = self.chats.find({})
        chats = [c['chat_id'] for c in ch]
        return chats
