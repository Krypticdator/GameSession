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

    def __str__(self):
        return str(self.__attributes)
                

    def get_all_attributes(self):
        '''for key, value in self.__attributes.items():
            print(str(key) + ' ' + str(value))'''
        return self.__attributes

class CyberItem(GameObject):
    def __init__(self, name, hum_cost=0, value=0, children=None):
        super().__init__()
        if children is None:
            children={}
        self.set_attribute('name', name)
        hum = self.validate_hum_cost(hum_cost)
       
        self.set_attribute('hum_cost', float(hum))
        self.set_attribute('value', value)
        self.set_attribute('options', children)

    def add_option(self, name, hum_cost=0, value=0):
        dictionary = self.get_attribute('options')
        dictionary[name] = CyberItem(name, hum_cost=hum_cost, value=value)

    def validate_hum_cost(self, hum_cost_text):
        hum = 0.0
        #print('hum_cost_text is ' + str(hum_cost_text))
        if type(hum_cost_text) is str:
            #print('if statement passed in hum validation')
            if hum_cost_text.count('/')>0:
                #print('hum_cost_text has / sign bigger than zero')
                array = hum_cost_text.split('/', 1)
                try:
                    hum = float(array[0])
                except Exception:
                    print('error ' + hum)
                    hum = 0
            else:
                try:
                    #print('else statement of validation')
                    hum = float(hum_cost_text)
                except TypeError:
                    print('error ' + hum_cost_text)
        #print('hum at the end of validation is ' + str(type(hum)) + ' ' + str(hum))
        return hum

        


