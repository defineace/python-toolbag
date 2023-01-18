import os

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

    # Get directory
    def getDirectory(self):
        return self.directory

    # Get filtered directory
    def getDirectory_filtered(self, filter):

        directory_filtered = []
        for result in self.directory:

            if(result.__contains__(filter)):
                directory_filtered.append(result)
        return directory_filtered

    # Get previewed directory file names of search and replace
    def getDirectory_previewSearchAndReplace(self, search, replace):
        directory_preview = []
        for result in self.directory:
            if(result.__contains__(search)):
                directory_preview.append(result.replace(search, replace))
            else:
                directory_preview.append(result)
        return directory_preview

    # Edit directory file names via search and replace
    def editDirectory_searchAndReplace(self, search, replace):
        updated = False
        for result in self.directory:
            if(result.__contains__(search)):
                # Variables
                original_name = result
                new_name = result.replace(search, replace)
                
                # Format Path
                path_formatted = self.path

                # Rename Result
                os.rename(path_formatted + original_name, path_formatted + new_name)
                updated = True
        return updated