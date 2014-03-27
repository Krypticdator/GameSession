class FileControl(object):
    """description of class"""

    def read_file_to_segments(self, filepath, separator, external_array = False):
        f = open(filepath, 'r')
        array = []
        for line in f:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(separator, -1)
            if external_array == False:
                self.segmented_file_array.append(rivitiedot)
            else:
                array.append(rivitiedot)
        f.close()
        if external_array:
            return array


