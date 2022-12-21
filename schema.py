import sqlite3

class Database():
    def __init__(self):
        pass

    def connect(self):
        self.con = sqlite3.connect("fish_dump.db")
        self.cur = self.con.cursor()

    def close(self):
        self.con.commit()
        self.con.close()
        
    def create_table(self, table, column):
        self.connect()
        s = f'''create table if not exists {table}{column}'''
        self.cur.execute(s)
        self.close()

    def create_schema(self):
        _schema_list = [["Region", """
                           """],
                        ["SubRegion", """
                        """],
                        ["StudyArea", """
                        """],
                        ["SurveyYear", """
                        """]]
                        ["SurveyDate", """
                        """],
                        ["Latitude", """
                        """],
                        ["Longitude", """
                        """],
                        ["Management", """
                        """]]
                        ["StructureType", """
                        """],
                        ["Family", """
                        """],
                        ["ScientificName", """
                        """],
                        ["CommonName", """
                        """]
                        ["Trophic", """
                        """],
                        ["FishLength", """
                        """],
                        ["FishCount", """
                        """],
                        ["SurveyYear", """
                        """]

        for i in _schema_list:
            self.create_table(i[0], i[1])
            #print(f'{i[0]} has been created')