class GameObject(object):
    """description of class"""
    def __init__(self, dictionary=True):
        if dictionary:
            self.__attributes = {}
        else:
            self.__attributes = []
            self.__keys = []


        self.dictionary = dictionary
        

    def set_attribute(self, name, value):
        if self.dictionary:
            self.__attributes[name] = value
        else:
            self.__attributes.append(value)
            self.__keys.append(name)

    def get_attribute(self, name):
        if self.dictionary:
            try:
                return self.__attributes[name]
            except Exception:
                return 0
        else:
            try:
                index = self.__keys.index(name)
                return self.__attributes[index]
            except Exception:
                return 0
    def destroy_attribute(self, name):
        try:
            if self.dictionary:
                del self.__attributes[name]
            else:
                self.__keys.remove(name)
                self.__attributes.remove(name)
        except Exception:
            print('could not delete')
                

    def get_all_attributes(self):
        return self.__attributes


