class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        for i, j in guards:
            matrix[i][j] = 'G'
        for i, j in walls:
            matrix[i][j] = 'W'
        
        visited_set = set()
        cnt = 0

        for guard in guards:
            i, j = guard
            curr_cell = matrix[i][j]
            keep = [i, j]

            # go up 
            while  i - 1 >= 0:
                adj = matrix[i-1][j]

                ind = '{i},{j}'.format(i=i-1, j=j)
                if adj == 0:
                    if ind not in visited_set:
                        cnt += 1
                        visited_set.add(ind)
                else:
                    break
                
                i -= 1
            
            # go down
            i, j = keep
            while  i + 1 < m:
                adj = matrix[i+1][j]

                ind = '{i},{j}'.format(i=i+1, j=j)
                if adj == 0:
                    if ind not in visited_set:
                        cnt += 1
                        visited_set.add(ind)
                else:
                    break
                
                i += 1
            
            # go left
            i, j = keep
            while  j - 1 >= 0:
                adj = matrix[i][j-1]

                ind = '{i},{j}'.format(i=i, j=j-1)
                if adj == 0:
                    if ind not in visited_set:
                        cnt += 1
                        visited_set.add(ind)
                else:
                    break
                
                j -= 1
            # go right
            i, j = keep
            while  j + 1 < n:
                adj = matrix[i][j+1]

                ind = '{i},{j}'.format(i=i, j=j+1)
                if adj == 0:
                    if ind not in visited_set:
                        cnt += 1
                        visited_set.add(ind)
                else:
                    break
                j += 1


            i, j = keep

        return m * n - cnt - len(walls) - len(guards)
