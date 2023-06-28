def designerPdfViewer(h, word):
    # Write your code here
    max_height = 0
    for char in word:
        index = ord(char) - ord('a')
        height = h[index]
        if height >= max_height:
            max_height = height
            
    area = max_height * len (word)
    
    return area
            
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = 'zaba'

print(designerPdfViewer(h, word))