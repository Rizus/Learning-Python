


class FileReader:
    def __init__(self, content):
        self.content = content


    def read(self):
        try:
            with open(self.content, "r") as f:
                content = f.read()
                return content
        except OSError:
            return"{}".format("")
