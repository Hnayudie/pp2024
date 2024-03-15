import os
import gzip
import pickle
import threading

class PersistenceManager:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save_data(self, filename, data):
        save_thread = threading.Thread(target=self._save_data_thread, args=(filename, data))
        save_thread.start()

    def _save_data_thread(self, filename, data):
        filepath = os.path.join(self.data_dir, filename)
        with gzip.open(filepath, "wb") as file:
            pickle.dump(data, file)

    def load_data(self, filename):
        filepath = os.path.join(self.data_dir, filename)
        if os.path.exists(filepath):
            with gzip.open(filepath, "rb") as file:
                return pickle.load(file)
        else:
            return None
