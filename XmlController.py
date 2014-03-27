import xml.etree.ElementTree as ET
import copy
class XmlController(object):
    """description of class"""
    def __init__(self):
        self.__elements = {}

    def create_root(self):
        name = str(name)
        self.__elements["root"] = ET.Element(name)
    def get_root(self):
        return self.__elements['root']

    def create_element(self, name):
        name = str(name)
        self.__elements[name] = ET.Element(name)
        

    def create_sub_element(self, child, parent):
        child = str(child)
        created = ET.Element(child)
        self.__elements[parent].append(created)
        self.__elements[child] = created

    def set_value(self, attribute, value, element):
        value = str(value)
        self.__elements[element].set(attribute, value)

    def set_text(self, text, element):
        text = str(text)
        self.__elements[element].text = text
        

    def save_file(self,filepath):
        tree = ET.ElementTree(self.__elements["root"])
        tree.write(filepath)

    def load_file(self, path):
        try:
            tree = ET.parse(path)
            
            self.root = tree.getroot()
            self.__elements['root']=self.root
            return tree
        except Exception:
            print('error')
            return 'error'
    
    def read_table_names(self):
        data = []
        names = []
        for node in self.root.iter("tables"):
            data = list(node)
        
        for table in data:
            names.append(str(table.get('name')))

        return names

    def read_table(self, table_name):
        data = []
        t = []
        for node in self.root.iter("tables"):
            data = list(node)
        
        for table in data:
            if table.get('name')==table_name:
                #print(table_name)
                options = list(table)
                for option in options:
                    a = []
                    a.append(option.get('from'))
                    a.append(option.get('to'))
                    a.append(option.text)
                    t.append(a)
                    #print(a)

        return copy.deepcopy(t)


    def get_dataset(self, collection_name, dictionary=True, sub_collection=False, tag_collection=False, tag_params = [], dict_tag_name='name'):
        data = []
        dict = {}
        for node in self.root.iter(collection_name):
            sub_elements = list(node)
            data = sub_elements

        if dictionary:
            for cell in data:
                dict[cell.get(dict_tag_name)] = cell.text
                #print(cell.tag)
            return dict

        if sub_collection:
            set = []
            for sub in data:
                temp = []
                temp.append(list(sub))
                for array in temp:
                    a=[]
                    set.append(a)
                    for cell in array:
                        a.append(cell.text)

            return set

        if tag_collection:
            set = []
            for cell in data:
                temp = []
                for param in tag_params:
                    temp.append(cell.get(param))
                set.append(temp)
            return set


        return data
        
        




