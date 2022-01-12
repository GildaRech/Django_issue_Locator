import os


class Localizer:
    """This class provides a method that seeks from a parent directory, patterns in html and python files.
       It is constructed with the default development environment or editor Vs code or another can be specified using editor=Editor_System_Command_Name
       e.g. one wants to search for the pattern : Gilda Rech in the project with parent directory "C:\\", then
       Localizer(editor="notepad")._search("K:\\", "Gilda Rech")
    """
    def __init__(self, editor="code") -> None:
        self.editor=editor
        if not self.editor or self.editor=="code": self.editor="code"
        pass

    def _search(self, dir, *args):
        """ function that walks through directories whose parent is dir and searches in python and html files for patterns in args"""
        self.dir=dir; self.files, self.args, self.dictio = os.listdir(self.dir), args, []; os.chdir(self.dir)
        for self.file in self.files:
            if os.path.isdir(self.file)==True:
                os.chdir(os.path.abspath(self.file))
                self._search(os.getcwd())
            else:
                if self.file.endswith(".py") or self.file.endswith(".html"):
                    with open(str(self.file), mode="r", encoding="utf-8") as open_f:
                        self.content=open_f.read()
                        for kword in self.args:
                            if kword in self.content:
                                self.dictio.append((self.file, os.path.abspath(self.file)))
                        open_f.close()
        if self.dictio:
            for result in self.dictio:
                k=self.editor+" "+result[1]
                print(k)
                os.system(k)

    def _search2(self, dir, kword):
        self.dir, self.kword = dir, kword
        self.all_files = list(); self.names=list()
        for (directory_path, directory_names, file_names) in os.walk(self.dir):
            self.all_files += [os.path.join(directory_path, _file) for _file in file_names if _file.endswith(".py")==True or _file.endswith(".html")==True]
            self.names+=[_file for _file in file_names if _file.endswith(".py")==True or _file.endswith(".html")==True]
        for file in self.all_files:
            with open(str(file), mode="r", encoding="utf-8") as open_f:
                self.content=open_f.read()
                if self.kword in self.content:
                    os.system(self.editor+" "+file)
                    if file.endswith(".html")==True:
                        self._search2(self.dir, self.names[self.all_files.index(file)]) # this opens the concerned view files rendering the templates


# Example
#Localizer(editor="code")._search("..\\Script_localize_issue_files", "info visit")
# To localize and automatically launch concerned files located in ...\\Script_localize_issue_files with patter "info visit"
#Localizer(editor="code")._search2("..\\test", "essai")
                   