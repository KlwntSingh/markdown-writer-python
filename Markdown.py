class Markdown():
    def __init__(self, path_to_file):
        self.f = open(path_to_file, 'w')
        self.__commited_lines = []
        self.__last_line = ''

    def __commit_last_line(func):
        def last_line_commiter(*args, **kargs):
            self = args[0]
            if len(args)>=2:
                self.__flush()
            return func(*args, **kargs)
        return last_line_commiter

    def __last_line_processor(func):
        def temp_processor(*args, **kargs):
            self = args[0]
            if len(args)>=2:
                return func(*args, **kargs)
            else:
                return func(self, self._last_line)
        return temp_processor

    def __flush(self):
        self.__commited_lines.append(self.__last_line)
        self.__last_line = ''

    def save(self):
        self.__flush()
        text = "\n".join(self.__commited_lines)
        self.f.write(text)
        self.f.flush()

    @__commit_last_line
    @__last_line_processor
    def header(self, text):
        formated_text = "# " + text
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def header3(self, text):
        formated_text = "### " + text
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def text(self, text):
        formated_text = text
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def bold(self, text):
        formated_text = "**" + text + "**"
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def italic(self, text):
        formated_text = "*" + text + "*"
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def blockquote(self, text):
        formated_text = "> " + text
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def code(self, text):
        formated_text = "`" + text + "`"
        self.__last_line = formated_text
        return self

    def line(self):
        formated_text = "___"
        self.__flush()
        self.__last_line = formated_text
        self.__flush()
        return self

    @__commit_last_line
    @__last_line_processor
    def ordered_list(self, items):
        formated_text = ''
        for i in range(len(items)):
            item = items[i]
            formated_text += str(i + 1) + '. ' + item
            formated_text += '\n'
        self.__last_line = formated_text
        return self

    @__commit_last_line
    @__last_line_processor
    def uordered_list(self, items):
        formated_text = ''
        for i in range(len(items)):
            item = items[i]
            formated_text += '- ' + item
            formated_text += '\n'
        self.__last_line = formated_text
        return self


if __name__ == "__main__":
    markdown = Markdown('test.md')
    markdown.header("Test").bold("testing2").save()
    markdown.italic('testing 123, ').uordered_list(['kulwant', 'singh']).save()
