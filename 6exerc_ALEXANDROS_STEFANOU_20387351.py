    class TreasureMap:
        def __init__(self, map):
            self.map = map
            self.rows = len(map)
            self.columns =  len(map[0]) if map else 0

        def create_hunter_map(self):
            hunter_map = []
            for value in range(self.rows):
                row = []
                for val in range(self.columns):
                    row.append('-')
                hunter_map.append(row)
            return hunter_map
        
        def update_hunter_map(self, hunter_map, row, col):
            if self.map[row][col] == 'x':
                hunter_map[row][col]= 'o'
                return 1
            else:
                hunter_map[row][col]= 'o'
                return  0
            


    class TresureHunter
        def __init__(self, name, treasure_map):
            self.name = name
            self.map = treasure_map
            self.treasures = 0
            self.hunter_map = treasure_map.create_hunter_map

        def move_on_map(self, row, col):
            result = self.treasure_map.update_hunter_map(self.hunter_map, (row,col))
            if result == 'x'
                self.treasures +=1
                
        def check_status(self):
            for row self_hunter_map:
                print(' '.join(row)
            print(self.treasures)
