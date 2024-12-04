import os
class directoryExplorer:
    def __init__( self, path ):
        self.path = path
        self.directory = os.listdir( path )
    def returnDirectory( self ):
        # Return list of directory contents
        return self.directory
    def returnDirectoryFiltered( self, filter):
        # Return list of directory contents filtered
        contents = []
        for result in self.directory:
            if(result.__contains__(filter)):
                contents.append(result)
        return contents

        