class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        size = len(image)
        for i in range(size):
            row_rev = image[i][::-1]
            row_rev = list(map(lambda pxl: 0 if pxl == 1 else 1, row_rev))
            image[i] = row_rev
        return image
        
