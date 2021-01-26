def checkArray(self,arr, pieces):
    if len(arr)==0:
        return True
    for index,piece in enumerate(pieces):
        if piece == arr[:len(piece)]:
            return checkArray(arr[len(piece):],pieces[:index] + pieces[index+1:])

def canFormArray(arr,pieces):
    sol = checkArray(arr,pieces)
    return sol

if __name__ == "__main__":
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    canFormArray(arr,pieces)

