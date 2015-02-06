import sqlite3
class SQLController(object):
    """description of class"""
    def __init__(self, database):
        try:
            self.db = sqlite3.connect(database)
            self.__database_name = database
        except Exception:
            print('error connecting to database: ' +database)
            self.db.close()
        finally:
            self.db.close()


        #cursor.execute('''SELECT name, email, phone FROM test''')
        #user1 = cursor.fetchone() #retrieve the first row
        #print(user1[0]) #Print the first column retrieved(user's name)
        #all_rows = cursor.fetchall()
        '''for row in all_rows:
            # row[0] returns the first column in the query (name), row[1] returns email column.
            #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
            pass''' 
    
    def connect(self):
        try:
            self.db = sqlite3.connect(self.__database_name)
        except Exception:
            self.close()
            print('error while connecting to database: ' + self.__database_name)

    def close(self):
        try:
            self.db.close()
        except Exception:
            print('failed to close database: ' + self.__database_name)
    
    def inject_custom_sql(self, statement):
        failed = False
        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute(statement)
            self.db.commit()
            return cursor
        except Exception:
            self.db.rollback()
            print('injection of custom sql statement failed')
            failed = True
        finally:
            self.close()
            return failed

    def unsafe_injection(self, statement, read_only=True, use_values=False, values='none'):
        self.connect()
        cursor = self.db.cursor()
        if use_values:
            cursor.execute(statement, values)
        else:
            cursor.execute(statement)
        if read_only:
            pass
        else:
            self.db.commit()
        return cursor
    
    def insert(self, table_name, headers, values):

        insert_statement = 'INSERT INTO ' +table_name + '('
        header_text = ''
        for header in headers:
            header_text = header_text + header + ', '
        header_text = header_text[:-2]
        header_text = header_text + ') '
        
        values_text = 'VALUES('
        for i in range(0, len(headers)):
            values_text = values_text + ':' + headers[i] + ', '
        values_text = values_text[:-2] + ')'

        statement = insert_statement + header_text + values_text

        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute(statement, values)
            self.db.commit()
        except Exception:
            self.db.rollback()
            print('error while inserting into db: ' + self.__database_name)
        finally:
            self.close()

    def create_table(self, table_name, headers, types, primary_key=True, primary_not_null=True, primary_auto_increment=True):
        sql_text = 'CREATE TABLE IF NOT EXISTS ' + table_name + '('
        values_text = ''
        if primary_key:
            primary_text = 'id INTEGER PRIMARY KEY '
            if primary_auto_increment:
                primary_text = primary_text + 'AUTOINCREMENT '
                if primary_not_null:
                    primary_text = primary_text + 'NOT NULL, '
                    for i in range(0, len(headers)):
                        if i==0:
                            values_text = headers[i] + ' ' + types[i] + ', '
                        else:
                            values_text = values_text + headers[i] + ' ' + types[i] + ', '
                    sql_text = sql_text + primary_text + values_text
                    sql_text = sql_text[:-2]
                    sql_text = sql_text + ')'
                    #print(sql_text)
        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute(sql_text)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('error while creating table: ' + table_name + ' in database: ' + self.__database_name)
            print(e)
        finally:
            self.close()

    def select(self, headers, table, use_condition=False, condition='none'):
        failed = False
        final = ''
        statement = 'SELECT '
        columns_text = ''
        for text in headers:
            columns_text = columns_text + text + ', '
        columns_text = columns_text[:-2]
        from_text = ' FROM ' + table
        where_text = ' WHERE '
        if use_condition:
            for key, value in condition.items():
                where_text = where_text + ':' + key
                
            final = statement + columns_text + from_text + where_text
            print(final)
        else:
            final = statement + columns_text + from_text

        
        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute(final, condition)
            self.db.commit()
        except Exception as e:
            failed=True
            print(e)
            return failed

        finally:
            self.close()
            return cursor

    def __del__(self):
        self.db.close()

class WeaponSqlController(SQLController):
    def __init__(self):
        super().__init__('data/weapon_blueprints')
        #'wa', 'con', 'av', 'dmg', 'shts', 'rof', 'rel', 'range', 'cost'
        headers = ['name', 'type',  'wa',   'con',  'av',   'dmg',  'ammo', 'shts', 'rof',  'rel',  'range', 'cost',   'weight','flags',   'options',       'alt_munitions', 'description', 'category']
        values  = ['TEXT', 'TEXT',  'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT',  'TEXT',   'TEXT',  'TEXT',    'TEXT',          'TEXT',          'TEXT',        'TEXT'    ]

        self.create_table('weapons', headers, values)

    def insert_weapon(self, name, type, wa, con, av, dmg, ammo, shts, rof, rel, range, cost, weight='NA', flags='NA', options='NA', alt_munitions='NA', description='NA', category='NA' ):
        
        headers = ['name', 'type', 'wa', 'con', 'av', 'dmg', 'ammo', 'shts', 'rof', 'rel', 'range', 'cost', 'weight', 'flags', 'options', 'alt_munitions', 'description', 'category']
        values = {'name':name, 'type':type, 'wa':wa, 'con':con, 'av':av, 'dmg':dmg, 'ammo':ammo, 'shts':shts, 'rof':rof, 'rel':rel, 'range':range, 'cost':cost, 'weight':weight, 'flags':flags, 'options':options, 'alt_munitions':alt_munitions, 'description':description, 'category':category}

        #self.insert('weapons', headers, values)
        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute('''SELECT name FROM weapons WHERE name=?''',(name,))
            try:
                data = cursor.fetchone()
                if data[0]==name:
                    #print(data[0] + ' == ' + name)
                    pass
                else:
            
                    self.insert('weapons', headers, values)
                    self.db.commit()
            except Exception:
                self.insert('weapons', headers, values)
                self.db.commit()
        except Exception as e:
            print("error in inserting weapon at WpnSQLController")
            print(e)
        finally:
            self.close()

    def print_weapons_table(self):
        try:
            self.connect()
            cursor = self.db.cursor()
            cursor.execute('''SELECT * FROM weapons''')
            all_rows = cursor.fetchall() 
            for row in all_rows:
                print('{0}: {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))
        except Exception as e:
            print(e)
        finally:
            self.close()
        
        



