import os, time

class augment_directoryExplorer:
    def __init__(self, path):
        self.path = path
        self.directory = os.listdir(self.path)

    # Set new path
    def updatePath(self, newPath):
        self.path = newPath
        self.directory = os.listdir(self.path)

    def getPath(self):
        return self.path

    # Get directory - Unfiltered
    def getDirectory(self):
        return self.directory

    # Get directory - filtered
    def getDirectory_filtered(self, filter):
        directory_filtered = []
        for result in self.directory:
            if(result.__contains__(filter)):
                directory_filtered.append(result)
        return directory_filtered


    # Get directory date created -  filtered
    def getDirectory_dateCreated_filtered(self, filter):
        directory_dateCreated = []
        for result in self.directory:
            if(result.__contains__(filter)):
                path = self.path + "/" + result
                directory_dateCreated.append(time.ctime(os.path.getctime(path)))
        return directory_dateCreated

    # Get directory date modified -  filtered
    def getDirectory_dateModified_filtered(self, filter):
        directory_dateModified = []
        for result in self.directory:
            if(result.__contains__(filter)):
                path = self.path + "/" + result
                directory_dateModified.append(time.ctime(os.path.getmtime(path)))
        return directory_dateModified


    # Get directory file type -  filtered
    def getDirectory_type_filtered(self, filter):
        directory_type = []
        for result in self.directory:
            if(result.__contains__(filter)):
                path = self.path + "/" + result
                if(os.path.isdir(path) == True):
                    directory_type.append("Folder")
                else:
                    directory_type.append("File")           
        return directory_type

    # Get directory Search and Replace Previewed - unfiltered
    def getDirectory_previewRename(self, search, replace, filter):
        directory_preview = []
        for result in self.directory:
            if(result.__contains__(search) and result.__contains__(filter)):
                directory_preview.append(result.replace(search, replace))
            else:
                directory_preview.append(result)
        return directory_preview

    # Get directory Search and Replace Previewed - filtered
    def getDirectory_previewRename_filtered(self, search, replace, filter):
        directory_preview = []
        for result in self.directory:
            if(result.__contains__(filter)):
                if(result.__contains__(search)):
                    directory_preview.append(result.replace(search, replace))
                else:
                    directory_preview.append("")
                
        return directory_preview

    # Edit directory file names via search and replace
    def editDirectory_fileRename(self, search, replace):
        updated = False
        for result in self.directory:
            if(result.__contains__(search)):
                # Variables
                original_name = result
                new_name = result.replace(search, replace)
                
                # Format Path
                self.format_path()
                path_formatted = self.path

                # Rename Result
                os.rename(path_formatted + original_name, path_formatted + new_name)
                updated = True
        return updated

    def format_path(self):
        if(self.path[-1] != "/"):
            self.path = self.path + "/"
            
