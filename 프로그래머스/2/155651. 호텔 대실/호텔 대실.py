def convertTime(t):
    h, m = map(int, t.split(":"))
    return 60*h + m

def solution(book_time):
    sortedBookTime = sorted([[convertTime(s), convertTime(e)+10] for s, e in book_time], key = lambda x: x[0])
    rooms = []
    
    for s, e in sortedBookTime:
        used = False
        for i in range(len(rooms)):
            if rooms[i] <= s:
                rooms[i] = e
                used = True
                break
        if not used:
            rooms.append(e)
        
    return len(rooms)
    