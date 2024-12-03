import os
class directoryExplorer:
    def __init__( self, path ):
        self.path = path
        self.directory = os.listdir( path )
    def getDirectory( self ):
        # Show Directory
        return self.directory
    def getDirectoryFiltered( self, filter):
        # Show Directory Filtered
        contents = []
        for result in self.directory:
            if(result.__contains__(filter)):
                contents.append(result)
        return contents
    
    def renameSearch( self, search ):
        # renameSearch
        pass
    def renameReplace( self, path ):
        # renameReplace
        pass