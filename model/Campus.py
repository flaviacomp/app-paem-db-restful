class Campus:
    def __init__(self, conn):
        self.conn = conn

    def get(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM campus")  # This line performs query and returns json result
        for x in cursor:
            print(x)
        """{'campus': [i[0] for i in cursor]}"""
        return {'campus': [i[0] for i in cursor]}  # Fetches first column that is Employee ID
