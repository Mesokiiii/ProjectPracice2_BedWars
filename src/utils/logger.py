class Logger:
    def log(self, text):
        file = open("logs/game.log", "a", encoding="utf-8")
        file.write(text + "\n")
        file.close()


logger = Logger()
